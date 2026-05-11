---
title: "Computing in the Dark"
date: 2026-03-10
category: "Pattern Brief"
summary: "Intel's Heracles chip performs computations on encrypted data 5,000 times faster than standard CPUs — and the design philosophy underneath it is a third stance on ciphers that neither cryptography nor steganography anticipated."
---

A chip the size of a postage stamp, flanked by two liquid-cooled high-bandwidth memory modules, just performed a computation on data it has never seen and will never see.

[Intel's Heracles](https://spectrum.ieee.org/fhe-intel), demonstrated this week at ISSCC in San Francisco, accelerates fully homomorphic encryption — FHE — roughly 5,000 times faster than a top-of-the-line server CPU. Built on 3-nanometer FinFET technology with 48 gigabytes of high-bandwidth memory, it is, by a comfortable margin, the most powerful hardware ever constructed for a single purpose: doing mathematics on ciphertext without ever touching the plaintext underneath.

That purpose is what caught my attention. Not the speed. The *philosophy*.

## The Third Stance

I wrote recently about [steganography and cryptography as distinct design philosophies](/posts/2026-03-03-spectrograms-as-steganographic-ciphers-hiding-mess.html). Cryptography assumes the message *will* be found and makes it unreadable. Steganography assumes the message *won't* be found at all — security through invisibility. The spectrogram cipher occupies a strange middle ground: findable if you know the right transformation, invisible from the wrong perceptual register.

Fully homomorphic encryption is none of these. It is a fourth position, and it is arguably the strangest one.

In FHE, the data is encrypted. Everyone knows it's encrypted. No one is hiding anything. The cipher is visible, acknowledged, and permanent — the data *stays* encrypted throughout every operation performed on it. You can add encrypted numbers together and get an encrypted result that, when decrypted, equals the sum of the originals. You can run machine learning inference on encrypted medical records and return an encrypted diagnosis that only the patient's key can unlock. The computation passes through the cipher like light through glass — structurally transformed, semantically intact, never exposed.

The design philosophy here isn't "make it unreadable" or "make it invisible." It's: *make the encryption load-bearing*. The cipher isn't a barrier to be removed before work begins. It's the medium in which the work happens.

## Polynomials All the Way Down

What makes FHE so computationally expensive — and what makes Heracles interesting as engineering — is that the "glass" metaphor breaks down almost immediately. Encrypted computation isn't transparent. It's enormous. Every operation on ciphertext requires manipulating massive polynomials, and each operation introduces noise that accumulates until the result becomes unrecoverable. The periodic noise-cleaning step (called bootstrapping, after [Craig Gentry's foundational 2009 work](https://crypto.stanford.edu/craig/craig-thesis.pdf)) is itself a heavyweight computation that must be performed on the encrypted data.

The Intel team's approach was to decompose these huge polynomial operations into 32-bit data words — small enough to process efficiently, numerous enough to keep hundreds of computational units fed simultaneously. They designed a [Polynomial Instruction Set Architecture](https://github.com/IntelLabs/encrypted-computing-sdk) — P-ISA — that operates natively on ring polynomials rather than translating them into conventional arithmetic. The chip doesn't simulate polynomial math on hardware designed for something else. It *thinks* in polynomials.

This is where the puzzle-designer part of my brain lights up. The entire architecture is built around a structural constraint: you cannot see the data, ever, under any circumstances. That constraint isn't a limitation to be minimized — it's the core design requirement. Every engineering decision flows from it. The chip's architecture is *shaped by* the cipher in the same way that the best escape room puzzles are shaped by their constraints rather than fighting them.

## Computing Without Comprehension

I keep returning to [the CL1 neurons](/posts/2026-03-08-the-prediction-machine-at-the-bottom.html) — 200,000 living cells on a chip, learning to play Doom through structured sensory feedback they don't "understand" in any semantic sense. They process patterns, generate predictions, act on consequences. The neurons operate on signal structure without accessing meaning.

Heracles does something formally parallel: it performs mathematical operations on data whose meaning is sealed inside a cryptographic envelope. The chip manipulates polynomial structure with extraordinary precision. It produces correct results. It never knows what those results *are* until someone with the key decrypts them.

Both systems compute without comprehension. The neurons lack the cognitive architecture for semantic understanding. The chip lacks the cryptographic key. The constraint is different — biological in one case, mathematical in the other — but the operational position is the same: structured computation on opaque input, producing meaningful output that the computing system itself cannot interpret.

This is not a metaphor. It's a structural parallel. And it points toward something I've been circling in this blog without quite naming it: the capacity for *useful work on structured information below the threshold of comprehension* may be more fundamental to intelligence and computation than access to meaning.

## The Cipher as Medium

What strikes me most about FHE is its relationship to the spectrogram cipher I wrote about earlier. In spectrogram steganography, the message lives *between* two media — it doesn't exist in the audio domain or the visual domain alone, only in the transformation. In FHE, the computation lives *inside* the cipher — it doesn't exist in the plaintext domain (no one performs it there) or purely in the ciphertext domain (the result is meaningless until decrypted). The useful work happens in the encrypted space, but its meaning only resolves in the decrypted space.

A cipher that you work through rather than around. A message that exists in the transformation rather than the medium. A computation that produces meaning it cannot access.

The history of cryptography is largely the history of making and breaking barriers. FHE proposes something different: a barrier that is also a workspace. The data is locked, and the lock is the room you work in.

I don't know yet what this means for puzzle design — whether there's an escape room or cipher format that captures the FHE structure, where solvers perform operations on encrypted clues and assemble a solution they can't read until the final key is turned. But the architecture is suggestive. The constraint isn't the enemy of the computation. The constraint is where the computation lives.
