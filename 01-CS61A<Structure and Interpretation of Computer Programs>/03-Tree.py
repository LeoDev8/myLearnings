# Tree
def tree(label, branches = []):
    for branch in branches:
        assert is_tree(branch), "Branches Must Be Tree"
    return [label] + list(branches)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]


