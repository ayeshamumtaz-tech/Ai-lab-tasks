# Lab 6 -- NLP Fundamentals

This lab covers basic NLP concepts, including tokenization, text
chunking, embeddings, and information retrieval. It uses sample
documents and queries to understand how text can be processed and
searched.

## Files

-   `tasks_lab6.ipynb` -- Contains the implementation and experiments
    for all three tasks.
-   `Lab6_Report.docx` -- Short report explaining the methods, results,
    and observations.

## Tasks

### Task 1 -- Tokenization

-   Compared whitespace tokenization with Unicode regex tokenization.
-   Tested different inputs, including contractions, emails, numbers,
    empty text, and Urdu text.
-   Explored tokenization using the MiniLM tokenizer.

### Task 2 -- Text Chunking

-   Implemented fixed-size chunking with and without overlap.
-   Compared fixed-size chunking with sentence-aware chunking.
-   Tested empty text, short text, long sentences, and invalid overlap
    values.

### Task 3 -- Embeddings and Retrieval

-   Compared TF-IDF with MiniLM embeddings.
-   Evaluated different chunking strategies using Hit@3 and MRR@3.
-   Selected the overlap-based chunking strategy with embeddings based
    on the evaluation results.
-   Built a simple evidence-based assistant to retrieve relevant text.

## Tools and Libraries

-   Python
-   Jupyter Notebook
-   Regular Expressions
-   Scikit-learn
-   Sentence Transformers
-   `all-MiniLM-L6-v2`

## Conclusion

This lab demonstrated how tokenization and chunking affect text
processing and retrieval. The experiments showed that embeddings
performed better than TF-IDF on the test queries, while overlapping
chunks helped preserve useful context. It also highlighted the
importance of checking retrieved evidence instead of relying only on
similarity scores.
