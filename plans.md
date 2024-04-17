# Basic thoughts about the app
Let's go from frontend to backend, from user experience features to technologies I'll have to implement to achieve them but with keeping in mind that its Python app.

## User Interface
- User open .epub book or on first stages prepared file with text from the book: one sentence per row.
- When start reading, on screen:
    - a) 
        - book text on background, 
        - current sentence is active and on top or in the bottom of it there is translation to user's native language
        - TTS activation by tapping the active sentence
        - buttons "next sentence" and "previous sentence" lead to appropriate sentence
    b)
        - only current sentence is shown
        - on top or in the bottom of the current sentence there is translation to user's native language
        - three buttons: "pronounce", "next sentence", and "previous sentence"
- Some features:
    - integration with anki app: there should be a simple way to add words or sentences to anki database, original text, translation, generated TTS
    - history of books that have been read
    - easy way to import .epub, fb2, and other books


## Background
- The app planned to be used on phones
- for iPhone use Pythonista app
- TTS
    - first sentence of the book:
        - apply translate to current text firstly
        - display first sentence with translation
        - apply TTS for current sentence and next one concurrently
        - while TTS is in the process display running gif or pseudogriphics to indicate that the app wasn't freeesd yet.
    - n-th sentence of the book:
        - on pressing "next" button following things happen concurrently:
            - display next sentence with translation
            - apply TTS to the next sentence
            - apply translate to the next sentence
- UI
    - Use ui library provided by Pythonista

## Errors and check-ups
- if any error happens during the process, show popup with error and buttons like "ok" and "print error and open the code"
- for alfa version prepared book should be .py file with list of strings structure inside; check the file when open in the app.
