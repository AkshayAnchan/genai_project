# genai_project

# Application Layer 
    ChatGpt , Cloude , Github Copilot , Perpelxity 

    ## - Prompting - Prompt Engineering 
    Ex: Zero Shot prompting 
        Few Shot Prompting 

# using Angetic Orchestration 
    ## Langchain and Langgraph , 
    ## CrewAI , Google ADK 

# Agent 
    LLM -- brain 
    Tools --  To handle frozen nature of model and unknown data/ buisness logics 
    Memory -- to handle stateless behaviour and make agent statefull 
    Planing -- Agent buisness logic 

# LLM - Constraints 
    1. stateless -- Q2 [Q1+A1+Q2--> LLM --> A2]
    2. frozen 
    3. one token at a time -- Output becomes input 

# LLM - PROPERTIES -- Parameter Tuning 
    1. BY DEFAULT MODELS ARE DETERMINISTIC  -- Temperature -1 to 1 
        As long is input is same output probabilty remains ssame 


## One Token At a time -- Probability Distribution 

    Question - what is 2+2 ?
    Answer -- The answer is 4.

                                        20 [10 Reserved for input 10 are reserved for output]
    Itteration          Input                               Model             Output 
    01             what is 2+2 ?                           --> LLM -->          The 
    02             what is 2+2 [ANS] The                   --> LLM -->          Answer 
    03             what is 2+2 [ANS] The Answer            --> LLM -->          is 
    04             what is 2+2 [ANS] The Answer is         --> LLM -->          4 
    05             what is 2+2 [ANS] The Answer is 4       --> LLM -->          . 
    05             what is 2+2 [ANS] The Answer is 4.      --> LLM -->          [END]--> Stopword 


    05             {what is 2+2} [ANS] The Answer is 4.      --> LLM -->          [END]


    aswer answered answering 
    answer ed ing
    learn  leanred learning 


## Tokenization 
    https://platform.openai.com/tokenizer



# Uniqe words [Model Vocabulary]
    learn 
    answer 
    earn 
    play 
    ing 
    ed 
    read 

    what is 2+2 ? --> LLM --> 

    Probabilty : 
                learn  - 0.001
                answer - 0.4
                earn   - 0.004
                play   - 0.2
                ing    - 0.007
                ed     - 0.0008
                read   - 0.0009
    
    Selected word -->  highest Probabilty. -> "answer"

    Probability Property 
        --> sum of all the categrories/words  will always be 1 


    DETERMINISTIC : 
        Z = X+Y 
        X = 15 
        Y = 20

        Z = 30 


    #1 what is 2+2 ?
            learn  - 0.001
            answer - 0.4    -- selected  
            earn   - 0.004
            play   - 0.2
            ing    - 0.007
            ed     - 0.0008
            read   - 0.0009

    #2 what is 2+2 ? [ANS] answer
            learn  - 0.001
            answer - 0.004
            earn   - 0.004
            play   - 0.001
            ing    - 0.005
            ed     - 0.6     -- Selected 
            read   - 0.0009



    make Non DETERMINISTIC Behaviour

    #1 what is 2+2 ?
            learn  - 0.001
            answer - 0.4     
            earn   - 0.004
            play   - 0.2. -- selected 
            ing    - 0.007
            ed     - 0.0008
            read   - 0.0009

    #2 what is 2+2 ? [ANS] play
            learn  - 0.001
            answer - 0.004
            earn   - 0.2. -- Selected 
            play   - 0.001
            ing    - 0.005
            ed     - 0.6     
            read   - 0.0009


    







    









