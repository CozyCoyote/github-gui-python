import resources
import types

consts = types.SimpleNamespace()
consts.FEATURE_BRANCH = 0
consts.BUGFIX_BRANCH = 1
consts.HOTFIX_BRANCH = 2
consts.POC_BRANCH = 3


def resolveBranchIcon(name):
    match filterBranch(name):
        case consts.FEATURE_BRANCH:
            return resources.loadSvg('ic-feather', 0.25)
        case consts.BUGFIX_BRANCH:
            return resources.loadSvg('ic-bug', 0.035)
        case consts.HOTFIX_BRANCH:
            # make the bug red
            return resources.loadSvg('ic-bug', 0.035)
        case consts.POC_BRANCH:
            # make the feather yellow?
            return resources.loadSvg('ic-feather', 0.25)
        case default:
            return resources.loadSvg('ic-feather', 0.25)

# TODO make it customizable
def filterBranch(name):
    if name.startswith("feature"):
        return consts.FEATURE_BRANCH
    if name.startswith("bugfix"):
        return consts.BUGFIX_BRANCH
    if name.startswith("hotfix"):
        return consts.HOTFIX_BRANCH
    if name.startswith("poc"):
        return consts.POC_BRANCH
    return consts.FEATURE_BRANCH
    