import ast

class CodeQualityChecker(ast.NodeVisitor):
    def __init__(self):
        self.function_lengths = []
        self.variable_names = set()
        self.used_variables = set()
        self.line_count = 0
        self.alerts = []

    def visit_FunctionDef(self, node):
        function_length = len(node.body)
        self.function_lengths.append(function_length)

        if ast.get_docstring(node) is None:
            self.alerts.append(f"Warning: Function '{node.name}' is missing a docstring.")

        self.generic_visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.variable_names.add(target.id)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.used_variables.add(node.id)
        elif isinstance(node.ctx, ast.Store):
            self.variable_names.add(node.id)


    def check(self):
        for length in self.function_lengths:
            if length > 20:
                self.alerts.append("Warning: Function is longer than 20 lines.")

        if self.line_count > 200:
            self.alerts.append("Warning: File is longer than 200 lines.")

        unused_variables = self.variable_names - self.used_variables
        for var in unused_variables:
            self.alerts.append(f"Warning: Variable '{var}' is assigned but never used.")

def analyze_code(file_content: str):
    checker = CodeQualityChecker()
    checker.line_count = len(file_content.splitlines())
    tree = ast.parse(file_content)
    checker.visit(tree)
    checker.check()
    return checker.alerts ,checker.function_lengths
