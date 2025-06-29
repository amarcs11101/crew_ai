## Assignment Overview ______________________________________________________________________________________________________
Overview: 

      In current market there are lot of patents getting filed on regular basis all over the
      world. Our customers used to spend lot of time to analyze those patents and figure it out which
      technology/innovation to focus on their new product development in future.

Assignment:

      Recommended / Predict future innovation/technology to adopt by going through last 3 years
      patent filed for a specific research area as example – Lithium Battery
      Implementation should be Agentic Workflow with GEN AI principle. Performance is the key metrics
      to consider and a cost effective model. You are open to using Lang chain Framework or CrewAI to
      develop the Agentic Workflow.
      Prepare the system architecture high level for the Agentic workflow about the assignment.

______________________________________________________________________________________________________
      #####################
      # API RUNNING STEPS #
      #####################
- pip install -r requirements.txt
- cd api
- uvicorn app.main:app --reload
____________________________________________________________________________________________________________
                                    AGENTS USAGE      

            STAGE 1:    Background Patent Preprocessing (Daily/Weekly Job)
                        Task	Description
                        Patent Search (last 3 years)	Using DuckDuckGo + Lens.org APIs to get links
                        Download & Clean	WebsiteReader loads page and extracts content
                        Embedding	Generate vector representations using LLM embeddings
                        Store	Save into FAISS Vector DB 
                        Caching Metadata (source, date, tags) saved in relational DB (Postgres/Mongo) 

            STAGE 2: Real-Time Query + Prediction
                        Step	Description
                        User Prompt	e.g., “What are upcoming innovations in lithium batteries?”
                        Vector Search Retrieves top-N relevant patents from precomputed DB
                        LLM Summarization	Summarize only retrieved documents
                        Trend Prediction	Use prompt chaining or agents to identify innovation trends
                        Output Show insights, forecasts, and recommendations

           
____________________________________________________________________________________________________________


                           ┌──────────────┐
                           │   Scheduler  │
                           └─────┬────────┘
                                 ▼
            ┌─────────────────────────────────────────────┐
            │   Preprocessing Pipeline (Nightly/Daily)    │
            │   - Patent Search (3 years)                 │
            │   - WebsiteReader                           │
            │   - Embedding Generator                     │
            │   - Vector Store (FAISS)                    │
            └─────────────────────────────────────────────┘

                          Real-time User Query
                                  │
                                  ▼
                      ┌────────────────────────┐
                      │     Retrieval Agent    │ ← Vector Search
                      └────────┬───────────────┘
                               ▼
                        ┌────────────────────────┐
                        │     Summarizer Agent   │ ← LLM Summary
                        └────────┬───────────────┘
                               ▼
                        ┌──────────────────────────┐
                        │  Predictor/Insight Agent │ ← Trend & Forecasting
                        └──────────────────────────┘
                               ▼
                         ┌────────────┐
                         │    UI/API  │
                         └────────────┘
