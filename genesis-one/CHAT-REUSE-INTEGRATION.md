# Genesis Chat — reuse-first integration decision

Goal: working iPhone-first general chat as soon as practical, zero new spend, without misrepresenting native model capability.

## Verified existing components (public GitHub inspection)
- `godsun108/Sovereign-Core/src/adapter.js`: `OpenAICompatibleAdapter` already implements a configurable model endpoint, messages and provenance response. Reuse; do not write a competing inference adapter.
- `godsun108/Sovereign-Core/INFERENCE.md`: server-side private inference endpoint architecture; strong/balanced/compact tiers are architectural targets, **not evidence of running services**.
- `godsun108/Sovereign-Core/genesis/CONVERSATION-CHARACTER.md`: existing conversational behavior and truthfulness standard.
- `godsun108/Sovereign-Core/genesis/NATIVE_CONVERSATION_RESEARCH.md`: native Genesis conversational intelligence is research-only; no deployed native chat claim.
- `godsun108/Command-center/sovereign/genesis-handoff.mjs`: existing handoff module (not yet inspected for live readiness).
- `genesis-one/chat.html`: local, offline UI shell; no connected model, no network requests.

## Chosen architecture
Use Sovereign-Core as the model and provider-neutral interface authority. Use Command Center as the private authenticated gateway, memory/tool authorization and operational observability layer **after verifying its existing implementation**. The Genesis Chat browser is an unprivileged client. It should send messages only to an authenticated same-origin/private gateway, never carry model API keys or direct private model URLs. The gateway reuses the Sovereign-Core adapter. Display the returned model/runtime provenance; never attribute external model output to native Genesis. Keep the experimental v35 engine and its frozen baseline separate from general conversation.

## Shortest responsible delivery sequence
1. Inspect Command Center's actual Genesis handoff and authenticated request routes and Sovereign-Core's inference smoke tests, then identify the smallest existing usable path.
2. Verify whether a working local model service is installed/running on the private computer. GitHub code alone does not prove this. If none exists, do not imply chat is operational or incur paid inference charges.
3. Implement only the missing adapter-to-gateway glue with explicit authentication, size limits, timeouts, provenance and no privileged actions.
4. Connect the existing Genesis Chat UI to that verified gateway; test multi-turn conversation, errors, privacy, and honest fallback.
5. Validate iPhone reachability on the intended private network and record actual model identity, latency and quality. Keep native Genesis improvement on its own measured research track.

## Boundaries
Local Victory/VictoryChain is authoritative and may contain private-only code. Do not sync local assets to public GitHub, publish prompts/keys, or automatically bridge private context. No new spending, no production promotion without verification. A UI shell is not a conversational model; an adapter class is not a deployed inference runtime.
