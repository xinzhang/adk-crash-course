from google.adk.agents import BaseAgent, SequentialAgent
from google.adk.agents import InvocationContext, AgentExecutionEvent

class ConditionalRouterAgent(BaseAgent):
    async def _run_async_impl(self, ctx: InvocationContext):
        # Read a value from the shared session state
        is_eligible = ctx.session.state.get("is_eligible")

        if is_eligible:
            # If the condition is met, run Agent 2
            agent_2 = self.find_agent("Agent2")
            await agent_2.run_async(ctx)
        else:
            # Otherwise, run Agent 3
            agent_3 = self.find_agent("Agent3")
            await agent_3.run_async(ctx)

        yield AgentExecutionEvent(...) # Yield events to update the UI
        