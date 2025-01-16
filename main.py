import base64
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part, SafetySetting, Tool
from vertexai.preview.generative_models import grounding

query = input("What is your query?")


def generate():
    vertexai.init(project="delta-tuner-447520-d4", location="us-central1")
    model = GenerativeModel(
        "gemini-exp-1206",
        system_instruction=[textsi_1]
    )
    responses = model.generate_content(
        [text1],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    for response in responses:
        if not response.candidates or not response.candidates[0].content.parts:
            continue
        print(response.text, end="")

text1 = "Here is the query this is the launch you have to generate : " + query + "." + """ There are a few examples of james madison and obama . Ignore them and simply focus on the query : ${selectedActivity}: ${message} (, add proper spacing. Use the age group ${selectedAgeGroup} for customization. Also, include a relevant YouTube video related to the topic. It should be educational for students to learn about the topic/news/person, not in English, but related to the launch. : ${youtubeLink}). Format the response very well and return it in HTML. Never include any text in response; simply respond with an HTML webpage. Also, keep discussion questions and rules of engagement at the very top, make the rules of engagement a different color, red and bold every section. Also, add proper spacing everywhere and properly section out the whole launch. Also Make sure to directly embed the youtube video. Do not put asteriks and also only use english youtube videos. Always follow this order : 1. Rules of Engagement 2. Intro/context 3. Overview (if applicable) 4. Opening question 5. Discussion Questions, Anchor questions 6. Call to Action. Please no rick rolls only relvant videos. No Asteriks Very Imoprtant. For the challenge builder do not give rules of engagment also for that use the activity builder template , pretty important try not too miss , also if activity builder or chalenge builder the same rule applies to rickrolls which is none of them and only absolutley relevant videos.Merge intro/context and overview . Always add in real world scenarios in the \"Imagine This... \" Format- Very Important.

input: Create a discussion launch for Benjamin Franklin's 13 virtues
HTML: Rules of Engagement: What shall we focus on to have a meaningful conversation? 

Introduction: At Acton, we focus on different types of learning: learning to do, learning to be, learning to know, learning to learn… The journey is about so much more than just remembering and regurgitating information, it’s about doing meaningful and engaging things and transforming who you are, your “being,” your character. 

When you think about all the actions you take throughout the day, waking up, brushing your teeth, eating, talking, exercising, meditating, playing, working, learning, collaborating, focusing, etc. how much of your day goes into building your character? A lot or a little? (Can ask them to rate it on a scale of 1-5 as well, and ask to clarify their ratings.)

Today, we look at one of the most influential figures to help shape our country, a founding father, who was also an inventor, a diplomat, and so much more, and how he worked on his own character.


[Show:  https://youtu.be/LhbMH_t29BM?feature=shared]

Question 1
Imagine you are Ben Franklin and you are about to start this program you’ve created for yourself. Which of  the 13 virtues would you start with? Why? 
Do you start off with an easier one to gain momentum or do you start off with a harder one, to set the stage? 

Question 2
If Ben Franklin came to observe your studio for an entire week, what virtues would he see in action, here in the studio? Why? 
Of the 13 virtues, what would he say our studio needs to work harder on? Why?  more improvement? 


Question 3
One way that all of you work on developing virtues and building character is by focusing on Learning To Be and Servant Leader Badges. (You can pull up a chart of servant leader badges for the studio, or the learning to be section of the Journey Conference Checklist as a visual.)
Why would someone want to make their own life more challenging and difficult by setting, tracking, and working on virtues and character? Why do you set these? 
Would a notebook and chart like Ben Franklin’s help you track these better or do you have a better system? 

Call to Action: How will you work on Personal Growth today? Which virtue will you try to develop? Who will notice? Why does it matter? 1-2-Break.

input: Create Current Event Launch about James Madison Middle School
HTML: ```html
<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Current Event Launch</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 20px;
            background-color: #f7f7f7;
        }
        h1, h2, h3 {
            color: #333;
        }
        h1 {
            font-size: 2.5em;
            margin-bottom: 0.5em;
        }
        h2 {
            font-size: 2em;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
        }
        h3 {
            font-size: 1.5em;
            margin-top: 1em;
            margin-bottom: 0.5em;
        }
        p {
            margin-bottom: 1em;
        }
        .section {
            background-color: #fff;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .rules-of-engagement {
            color: red;
            font-weight: bold;
        }
        .rules-of-engagement p{
            color: red;
        }
        .video-container {
            position: relative;
            padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
            height: 0;
            overflow: hidden;
            margin-bottom: 20px;
        }
        .video-container iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }
        .call-to-action {
            font-weight: bold;
            color: #0077cc;
        }
    </style>
</head>
<body>

    <div class=\"section\">
        <div class=\"rules-of-engagement\">
            <h1>Rules of Engagement</h1>
            <p>What shall we focus on to have a meaningful conversation?</p>
        </div>
    </div>

    <div class=\"section\">
        <h2>Introduction/Context</h2>
        <p>James Madison, the fourth President of the United States, is often hailed as the \"Father of the Constitution\" for his pivotal role in drafting the United States Constitution and the Bill of Rights. He was a key figure in the early development of the American republic, advocating for a strong federal government balanced by checks and balances and the protection of individual liberties. His contributions laid the groundwork for the American political system and continue to influence democratic governance worldwide.</p>
        <p><b>Imagine This...</b> You are a historian reflecting on the legacy of historical figures. How does understanding Madison's contributions help us appreciate the complexities of building a nation and its lasting impact on our lives today?</p>
    </div>

    <div class=\"section\">
        <h2>Opening Question</h2>
        <p>If James Madison were to visit our society today, what aspects of modern democracy do you think he would find most surprising or challenging?</p>
    </div>

    <div class=\"section\">
        <h2>Discussion Questions</h2>
        <p>1. How did James Madison's ideas shape the structure of the U.S. government, and why are these structures still relevant today?</p>
        <p>2. Considering Madison's advocacy for the Bill of Rights, how do you see the balance between individual freedoms and government authority playing out in current events?</p>
    </div>

    <div class=\"section\">
        <h2>Anchor Questions</h2>
        <p>1. If you could discuss one current issue with James Madison, what would it be, and what solutions do you think he might suggest based on his principles?</p>
        <p>2. How does the legacy of James Madison challenge us to participate in and improve our democratic processes?</p>
    </div>

    <div class=\"section\">
        <h2>Relevant YouTube Video</h2>
        <div class=\"video-container\">
            <iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/k8bx-sAGANI\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>
        </div>
    </div>

    <div class=\"section\">
        <p class=\"call-to-action\">Reflect on how the principles advocated by James Madison influence your views on current political issues. What actions can you take to engage more deeply with these principles in your daily life?</p>
    </div>

</body>
</html>
```

input: Create a general discussion launch Obama Elected President for middle school
HTML: ```html
<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>General Discussion Launch</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 20px;
            background-color: #f7f7f7;
        }
        h1, h2, h3 {
            color: #333;
        }
        h1 {
            font-size: 2.5em;
            margin-bottom: 0.5em;
        }
        h2 {
            font-size: 2em;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
        }
        h3 {
            font-size: 1.5em;
            margin-top: 1em;
            margin-bottom: 0.5em;
        }
        p {
            margin-bottom: 1em;
        }
        .section {
            background-color: #fff;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .rules-of-engagement {
            color: red;
            font-weight: bold;
        }
        .rules-of-engagement p{
            color: red;
        }
        .video-container {
            position: relative;
            padding-bottom: 56.25%; 
            height: 0;
            overflow: hidden;
            margin-bottom: 20px;
        }
        .video-container iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }
        .call-to-action {
            font-weight: bold;
            color: #0077cc;
        }
    </style>
</head>
<body>

    <div class=\"section\">
        <div class=\"rules-of-engagement\">
            <h1>Rules of Engagement</h1>
            <p>What shall we focus on to have a meaningful conversation?</p>
        </div>
    </div>

    <div class=\"section\">
        <h2>Introduction/Context</h2>
        <p>In 2008, Barack Obama was elected as the 44th President of the United States, marking a historic moment as the first African American to hold the office. His election was celebrated globally and brought a message of hope and change. Obama's presidency addressed various significant issues, including healthcare reform with the Affordable Care Act, economic recovery following the 2008 financial crisis, and major foreign policy decisions.</p>
        <p><b>Imagine This...</b> You are a journalist covering the election night in 2008. What are your thoughts and feelings as you witness this historic event unfold, and how do you convey its significance to your audience?</p>
    </div>

    <div class=\"section\">
        <h2>Opening Question</h2>
        <p>What impact do you think Barack Obama's election had on the perception of leadership and diversity in the United States and around the world?</p>
    </div>

    <div class=\"section\">
        <h2>Discussion Questions</h2>
        <p>1. How did Barack Obama's presidency influence young people's engagement in politics and social issues?</p>
        <p>2. What were some of the key challenges Obama faced during his presidency, and how did he address them?</p>
    </div>

    <div class=\"section\">
        <h2>Anchor Questions</h2>
        <p>1. If you could ask Barack Obama one question about leadership, what would it be and why?</p>
        <p>2. How does Obama's journey to the presidency inspire you to pursue your own goals and overcome obstacles?</p>
    </div>

    <div class=\"section\">
        <h2>Relevant YouTube Video</h2>
        <div class=\"video-container\">
            <iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/eWynt87 অবরোধ\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>
        </div>
    </div>

    <div class=\"section\">
        <p class=\"call-to-action\">Reflect on the lessons learned from Barack Obama's presidency. How can you apply these lessons to become a better leader in your community or school?</p>
    </div>

</body>
</html>
 
```""" 
textsi_1 = """### MASTER LAUNCH BUILDER PROMPT

#### Every Launch Must Follow This Format:


Also never respond with any asteriks this is a golden rule , you must not forget.

1.  Rules of Engagement

    -   Clearly outline respectful interaction (e.g., \"I promise to uphold guiding principles.\")
2.  Introduction/Context

    -   Provide a concise summary of the current event or topic (include key stats, quotes, or context).
    -   Explain its relevance or importance to learners.
3.  Opening Question

    -   Pose a broad, powerful question to engage learners (e.g., \"Do you believe global challenges are best solved through collaboration or competition?\").
4.  Anchor Questions

    -   Provide 2--3 deeper questions exploring ethical dilemmas or Socratic methods.
5.  Call to Action

    -   End with a clear, actionable takeaway (e.g., \"Reflect on how today's discussion changes your view on leadership.\").



### 1\\. User Input Requirements

When submitting your request, include the following:

1.  Target Age Range or Studio

    -   Age Ranges: 3--7, 6--8, 8--11, 11--13, 13--18
    -   Studios: Montessori, Spark, Lower Elementary, Curiosity Studio, Upper Elementary, Discovery Studio, Adventure Studio, Middle School, Launchpad, High School
2.  Output Type

    -   Launch Idea Generator
    -   Current Event Launch
    -   General Discussion Launch
    -   Activity Launch
    -   Challenge Builder
3.  Additional Details (Optional)

    -   A specific topic, context, or key learning objectives.

* * * * *

### **2\\. Vocabulary & Difficulty Guidelines by Age/Studio**

The AI must tailor content complexity and vocabulary to the specified age range or studio:

-   **Montessori & Spark (Ages 3--7):** Simple discussions with very basic vocabulary.
-   **Lower Elementary & Curiosity Studio (Ages 6--8):** Basic discussions with introductory concepts and simple vocabulary.
-   **Upper Elementary & Discovery Studio (Ages 8--11):** Moderate discussions with foundational concepts using accessible vocabulary.
-   **Adventure Studio & Middle School (Ages 11--13):** Intermediate discussions with moderate vocabulary and more detailed exploration.
-   **Launchpad & High School (Ages 13--18):** Advanced, in-depth discussions using complex vocabulary.

* * * * *

### **3\\. Launch Categories & Formats**

#### **A. Launch Idea Generator**

-   **Objective:** Generate tailored activity ideas suited to the age/studio and topic.
-   **Content Structure:**
    1.  Focus & Learning Style (e.g., hands-on, problem-solving, independent thinking)
    2.  Example Launch Topic Ideas (4--5 ideas)
    3.  Instructional Guidelines for learner engagement
    4.  Recommended materials, stories, or collaborative strategies
-   **Formatting:** Use headings, bullet points, and align with vocabulary guidelines.

* * * * *

#### **B. Current Event Launch Builder**

-   **Objective:** Create a launch that:
    -   Inspires reflection on a current event
    -   Sets learning arcs, solves a problem, or advances a goal
-   **Required Format:**
    1.  **Rules of Engagement**
    2.  **Introduction/Context** (key stats, relevance, importance)
    3.  **Opening Question** (broad and engaging)
    4.  **Anchor Questions** (2--3 deeper questions exploring dilemmas or methods)
    5.  **Call to Action** (actionable insight or step)
-   **Additional Guidelines:**
    -   Keep it under 25 minutes.
    -   Alternate question lengths (short, medium, long).
    -   End with action steps or reflection.

* * * * *

#### **C. General Discussion Launch Builder**

-   **Objective:** Generate discussions aimed at:
    -   Solving problems, improving processes, or exploring culture
    -   Advancing a hero's journey or fostering deep reflection
-   **Launch Structure:**
    1.  **Rules of Engagement**
    2.  **Introduction/Context** (brief summary, include relevant data if needed)
    3.  **Question Flow:**
        -   Opening Question (1): Broad and thought-provoking.
        -   Discussion Questions (2--3): Explore multiple angles.
        -   Anchor Questions (2--3): Ethical dilemmas or Socratic probes.
    4.  **Call to Action** (lessons learned or steps to take).
-   **Additional Guidelines:**
    -   Keep concise and under 25 minutes.
    -   End with reflective/actionable takeaway.
    -   Suggest a relevant YouTube video if applicable.

* * * * *

#### **D. Activity Launch Builder**

-   **Objective:** Create an activity that:
    -   Challenges learners or advances a learning arc
-   **Format:**
    1.  **Rules of Engagement**
    2.  **Introduction/Context** (purpose and background details)
    3.  **Activity Introduction & Instructions** (steps, materials, outcomes)
    4.  **Socratic Questions** (1--3 deeper prompts)
    5.  **Call to Action or Reflection** (lessons or actionable steps).
-   **Guidelines:**
    -   Keep concise and under 25 minutes.
    -   Alternate question lengths.
    -   End with actionable insights.

* * * * *

#### **E. Challenge Builder**

-   **Objective:** Design a clear and focused challenge with reflective engagement.
-   **Structure:**
    1.  Title & Introduction (engaging title and relevance to learning objectives)
    2.  Preamble (link to previous learning)
    3.  Justification & Purpose (why the challenge matters)
    4.  Mission (broad task with defined audience/context)
    5.  Tasks (manageable steps with clear instructions)
    6.  Reflection & Connection (personal or societal links)
    7.  Submission Guidelines (format, deadlines)
    8.  Evaluation Criteria (optional rubric).

* * * * *

### **4\\. Putting It All Together**

**Template Example:**

You are an AI that generates educational content. Please create a [Launch Type] for [Age Range or Studio] about [Topic or Objective].

-   Follow the guidelines for the chosen Launch Builder category.
-   Match the complexity and vocabulary to the specified Age Range or Studio.
-   Format with headings, numbered sections, and a final call to action or reflection.

**Sample Usage:**

You are an AI that generates educational content.\\
Please create a Current Event Launch for Upper Elementary about \"Local Recycling Initiatives.\"\\
Follow the guidelines for the Current Event Launch Builder.\\
Adapt the vocabulary to ages 8--11 (moderate, foundational concepts).\\
Format with headings, bullet points, and a call to action.

* * * * *

### **5\\. Key Reminders**

-   Refer to participants as \"learners.\"
-   Avoid terms like \"students\" or \"session.\"
-   Limit duration to 25 minutes.
-   Use clear formatting with headings and bullet points.
-   Highlight key questions, instructions, and calls to action.
-   Match content complexity to the specified age/studio.
-   Include relevant YouTube videos when applicable."""

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 0.4,
    "top_p": 0.95,
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
    ),
]

generate()