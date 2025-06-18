
from pathlib import Path

#ADK imports
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset , StdioServerParameters

#Local imports
from .prompt import API_MCP_PROMPT

#IMPORTANT: There is a bug where relative path doesn't work when running local mcp servers.
#In this case, we use the absolute path.
PATH_TO_MCP_SERVER = ruta_archivo = str((Path(__file__).parent.parent / 'mcp_server' / 'server.py').resolve())



root_agent = LlmAgent(
    name="api_mcp_client_agent",
    description="Agent for interacting with the APIs",
    model="gemini-2.0-flash",
    instruction = API_MCP_PROMPT,
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command="python3",
                args=[PATH_TO_MCP_SERVER]
        ))

    ],
)