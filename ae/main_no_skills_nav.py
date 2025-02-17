import asyncio

from ae.core.system_orchestrator import SystemOrchestrator

if __name__ == "__main__":
    orchestrator = SystemOrchestrator(agent_scenario="user_proxy,browser_nav_agent_no_skills",input_mode="GUI_ONLY")
    asyncio.run(orchestrator.start())
