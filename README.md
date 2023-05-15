# FM Radio Receiver in GNU Radio 

This project is a simple implementation of an FM receiver using GNU Radio, a free & open-source software development toolkit. 

## About

The receiver has been implemented to demodulate frequency modulated signals, specifically designed to work with Convergent Digital Radio (CDR) signals. 

The CDR system we're targeting operated at a frequency of 106.1 MHz, with a bandwidth of 400 kHz. The Radio Telephone Network C (C-Netz), a first generation analog cellular phone system deployed and operated in Germany, was a specific use case for this implementation.

## How It Works

The receiver uses a flow graph in GNU Radio Companion (GRC). The flow graph takes an input file (in .wav format), processes it using a series of blocks (for decimation, demodulation, filtering, etc.), and outputs the demodulated signal into a .wav file.

The main blocks used in this implementation include:

- Wav File Source
- Throttle
- Rational Resampler
- Low Pass Filter
- Quadrature Demod
- Symbol Sync
- Binary Slicer
- Wav File Sink

## Requirements

- GNU Radio
- Python
- A WAV file containing CDR data

## Usage

1. Clone the repository.
2. Open the GRC file in GNU Radio Companion.
3. Set the parameters in each block according to your specific requirements.
4. Run the flow graph to process your input file and generate the output file.

## Notes

This project is a demonstration of using GNU Radio for signal processing. The quality of the output depends on the quality of the input signal, as well as the accuracy of the parameters set in the flow graph.
