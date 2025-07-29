#!/usr/bin/env python
from random import randint
from pydantic import BaseModel
from crewai.flow import Flow, listen, start
from sample_flow.crews.poem_crew.poem_crew import PoemCrew
import httpx
from keboola.component import CommonInterface, UserException
import os


class PoemState(BaseModel):
    sentence_count: int = 1
    poem: str = ""


class PoemFlow(Flow[PoemState]):

    @start()
    def generate_sentence_count(self):
        print("Generating sentence count")
        self.state.sentence_count = randint(1, 5)

    @listen(generate_sentence_count)
    def generate_poem(self):
        print("Generating poem")
        result = (
            PoemCrew()
            .crew()
            .kickoff(inputs={"sentence_count": self.state.sentence_count})
        )

        print("Poem generated", result.raw)
        self.state.poem = result.raw

    @listen(generate_poem)
    def save_poem(self):
        print("Saving poem")
        os.makedirs("/data/out/files", exist_ok=True)
        with open("/data/out/files/poem.txt", "w") as f:
            f.write(self.state.poem)


def kickoff():
    ci = CommonInterface()
    params = ci.configuration.parameters
    os.environ["OPENAI_API_KEY"] = params.get("#OPENAI_API_KEY")
    poem_flow = PoemFlow()
    poem_flow.kickoff()


def plot():
    poem_flow = PoemFlow()
    poem_flow.plot()


if __name__ == "__main__":
    kickoff()
