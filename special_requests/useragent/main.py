from random import randrange
from collections import namedtuple


_AGENTS_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0",
    "Mozilla/5.0 (Android 8.0; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0",
    "Mozilla/5.0 (Android 8.0; Tablet; rv:41.0) Gecko/41.0 Firefox/41.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/59.0",
    "Mozilla/5.0 (iPod touch; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) FxiOS/1.0 Mobile/12F69 Safari/600.1.4",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) FxiOS/1.0 Mobile/12F69 Safari/600.1.4",
    "Mozilla/5.0 (iPad; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) FxiOS/1.0 Mobile/12F69 Safari/600.1.4"
]

class UserAgentMixin:
    def get_user_agent(self, agent_index=0):
        return _AGENTS_LIST[agent_index]

    def get_user_agents(self):
        agents = namedtuple('Agents', ['headers'])
        return agents(_AGENTS_LIST)

    def get_rand_user_agent(self):
        agent_list_lenght = len(_AGENTS_LIST)
        return _AGENTS_LIST[randrange(0, agent_list_lenght)]
        