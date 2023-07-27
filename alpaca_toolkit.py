from abc import ABC
from typing import Any, Dict, List
from pydantic import BaseModel
from superagi.tools.base_tool import BaseToolkit, BaseTool

class AlpacaTool(BaseToolkit, ABC):
    name: str
    description: str
    tools: List[BaseTool]

    class Config:
        arbitrary_types_allowed = True

    def get_tools(self) -> Dict[str, Any]:
        return {tool.name: tool for tool in self.tools}

    def get_tool(self, name: str) -> BaseTool:
        return self.get_tools()[name]

tools = [AlpacaTool(name='AlpacaTool', description='Description')]
toolkit = BaseToolkit(name='AlpacaToolkit', description='Description', tools=tools)

