# Portable SENSE Memory

SENSE v0.3 can export its local capture memory as a human-readable JSON file and import that file into another browser/device. Imports require the `edge.sense.export.v1` schema and deduplicate by capture ID.

This is a bridge, not cloud sync. The user explicitly moves the file; EDGE does not upload captures to a server. This makes local-first memory portable before a private authenticated sync service exists.

A future native iOS companion should use the same logical capture schema so web and native clients can exchange data without changing the meaning of captures.
