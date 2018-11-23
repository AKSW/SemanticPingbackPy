#!/usr/bin/env python3

import semanticpingback

sp = semanticpingback.SemanticPingbackReceiver()
links = sp.receivePing("http://resource.feedback.aksw.org/dda9890831d7f16b598eb7f854afeb71-resource", "http://mmoon.org/lang/heb/inventory/oh/Lexeme_אֱגוֹז")
print(links.serialize(format="nt").decode("utf-8"))
