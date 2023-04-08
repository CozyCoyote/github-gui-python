from github import Github
import settings


class Api:

    g = None

    def connect(self):
        self.g = Github(settings.token())

        # host = settings.hostname()

        # Github Enterprise with custom hostname
        # self.g = Github(base_url="https://github.com/api/v3", login_or_token=settings.token())
        # self.g = Github(settings.userName(), settings.password())

    def listRepos(self):
        # repo = self.g.get_repo("PyGithub/PyGithub")
        # user = self.g.get_user()
        # user.login
        # # print(user)

        # for repo in self.g.get_user().get_repos() :
        #     print(repo.name)
        return self.g.get_user().get_repos()

    def listPullRequests(self,full_name):
        return self.g.get_repo(full_name).get_pulls(state='open')
