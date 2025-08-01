from google.adk.sessions import InMemorySessionService, Session

temp_service = InMemorySessionService()

example_session: Session = temp_service.create_session(
  app_name="my_app",
  user_id="example_user",
  state={"initial_key": "initial_value"}
)

print(example_session)

