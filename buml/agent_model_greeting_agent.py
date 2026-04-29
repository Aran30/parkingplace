###############
# AGENT MODEL #
###############
import datetime
from besser.BUML.metamodel.state_machine.state_machine import Body, Condition, ConfigProperty, CustomCodeAction
from besser.BUML.metamodel.state_machine.agent import Agent, AgentReply, LLMReply, RAGReply, DBReply, LLMOpenAI, LLMHuggingFace, LLMHuggingFaceAPI, LLMReplicate, RAGVectorStore, RAGTextSplitter, ReceiveTextEvent, ReceiveFileEvent, ReceiveJSONEvent, ReceiveMessageEvent, WildcardEvent, DummyEvent
from besser.BUML.metamodel.structural import Metadata
import operator

agent = Agent('Greeting_Agent')

agent.add_property(ConfigProperty('websocket_platform', 'websocket.host', '0.0.0.0'))
agent.add_property(ConfigProperty('websocket_platform', 'websocket.port', 8765))
agent.add_property(ConfigProperty('websocket_platform', 'streamlit.host', '0.0.0.0'))
agent.add_property(ConfigProperty('websocket_platform', 'streamlit.port', 5000))
agent.add_property(ConfigProperty('nlp', 'nlp.language', 'en'))
agent.add_property(ConfigProperty('nlp', 'nlp.region', 'US'))
agent.add_property(ConfigProperty('nlp', 'nlp.timezone', 'Europe/Madrid'))
agent.add_property(ConfigProperty('nlp', 'nlp.pre_processing', True))
agent.add_property(ConfigProperty('nlp', 'nlp.intent_threshold', 0.4))
agent.add_property(ConfigProperty('nlp', 'nlp.openai.api_key', 'YOUR-API-KEY'))
agent.add_property(ConfigProperty('nlp', 'nlp.hf.api_key', 'YOUR-API-KEY'))
agent.add_property(ConfigProperty('nlp', 'nlp.replicate.api_key', 'YOUR-API-KEY'))

# INTENTS
greeting_intent = agent.new_intent('Greeting_intent', [
    'Hi',
    'Hello',
    'Howdy',
],
)
good_intent = agent.new_intent('Good_intent', [
    'Good',
    'Fine',
    'I\\\'m alright',
],
)

# Create LLM instance for use in state bodies
llm = LLMOpenAI(agent=agent, name='gpt-4o-mini', parameters={})

# STATES
initial = agent.new_state('initial', initial=True)
greeting = agent.new_state('greeting')
good = agent.new_state('good')

# initial state
initial.when_intent_matched(greeting_intent).go_to(greeting)

# greeting state
greeting_body = Body('greeting_body')
greeting_body.add_action(AgentReply('Hi!'))
greeting_body.add_action(AgentReply('How are you?'))

greeting.set_body(greeting_body)
greeting.when_intent_matched(good_intent).go_to(good)

# good state
good_body = Body('good_body')
good_body.add_action(LLMReply())

good.set_body(good_body)
good.go_to(initial)

