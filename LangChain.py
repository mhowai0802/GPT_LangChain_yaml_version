def openai(self):
        llm_openai = AzureChatOpenAI(deployment_name=os.environ["GPT_VERSION"],temperature=0,openai_api_version=os.environ["OPENAI_API_VERSION"])
        tools = NLAToolkit.from_llm_and_url(llm_openai, "https://currency-conversion-plugin--mhowai0802.repl.co/.well-known/openapi.yaml").get_tools()
        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        agent_chain_openai = initialize_agent(tools, llm_openai, agent="chat-conversational-react-description",verbose=True, memory=memory)
        return agent_chain_openai
