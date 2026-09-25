# EDGE Inbox

RADAR observations can be triaged locally as **NEW**, **WATCHING**, **REVIEWED**, **SAVED**, or **DISMISSED**.

The browser stores triage state in localStorage under `edge.inbox.v1`. This is intentionally local-first: no account, server database, or personal triage history is published to the public repository.

Dismissed items leave the active queue; watching/reviewed/saved states remain visible with their state. Source observations and human triage remain separate data layers.

Future private deployments can sync this state across devices without changing the public observation pipeline.
