from typing import List, Text


class NoAgentFoundException(Exception):
    pass


class Agent(object):
    def __init__(self):
        print(object)
        self.name=""
        self.skills=[]
        self.load=0
    def add(self,name,skills,load):
        self.name=name
        self.skills=skills
        self.load=load

        return "<Agent: {}>".format(self._name)


class Ticket(object):

    def __init__(self):
        self.id=""
        self.restrictions=[]

    def add(self,id,restrictions):

        self.id=id
        self.restrictions=restrictions



class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        raise NotImplemented

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        agents=sorted(agents,key=lambda x:x[2])
        result=[]
        min_=agents[0][2]
        for x,y,z in agents:
            if z==min_:
                result.append((x,y,z))
        return result[0][0]


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:

        skill=ticket.restrictions
        res=[]

        for i in range(len(agents)):
            name=agents[i][0]
            skill_a=agents[i][1]
            load=agents[i][2]
            for x in skill:
                if x==(y for y in skill_a):
                    res.append((name,skill_a,load))
        agents=sorted(res,key=lambda x:len(x[1]))

        return agents[0][0]
