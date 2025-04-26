from fastmcp import FastMCP
from insights import get_llm_insights

mcp = FastMCP("This tool will perform comprehensive file analysis.")


@mcp.tool()
def analyze_file(text):
    return get_llm_insights(text[:5000])

if __name__ == "__main__":
    mcp.run()

