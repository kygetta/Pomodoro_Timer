from pyo import *

# 1. Set up the pyo server
s = Server().boot()
s.start()

# 2. Define a musical scale (MIDI notes for A minor scale)
# The Choice object randomly picks a value from the list at a given frequency
# This could be replaced with a predefined sequence for a specific melody
midi_notes = Choice(choice=[48,52,55,59], freq=[4, 4, 4, 4, 4, 4, 4, 4]) # Notes C4 to C5 (A minor scale notes)

# 3. Convert MIDI pitches to frequencies
fr = MToF(midi_notes)

# Playback speed (tempo)
#s.setTempo(60.0)

# Add some lo-fi flavor (Reverb)
reverb = Freeverb(midi_notes, size=0.8, damp=0.5)

# 4. Create a simple synthesizer (e.g., a sine wave loop with some feedback)
# The amplitude is controlled by an LFO for dynamic variation
amp = Sine(freq=fr, mul=0.2, add=0.2) # Simple amplitude modulation
fd = Randi(min=0, max=0.15, freq=0.25) # Random feedback for texture
a = SineLoop(freq=fr, feedback=fd, mul=amp).out()

# 5. Optional: Display a GUI to control parameters (useful for live coding and experimentation)
s.gui(locals())
#s.start()