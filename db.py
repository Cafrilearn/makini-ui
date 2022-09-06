from subjects.science.human_body import reproductive_system
from subjects.science.human_body import heart
from subjects.science.human_body import digestive_system

from subjects.financial_literacy import blockchain



content_detail = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. \n
Kadim Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. \n
Humeai Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n
"""

evolution_of_money = """
People have used money for more than 4,000 years. In the 600s bce the kingdom of Lydia in what is now Turkey began to make coins. It was probably the first government to do so. These coins were a combination of silver and gold, called electrum. Many ancient peoples, including the Greeks and the Romans, also used coins.\n
The first types of paper money were used in China more than 1,000 years ago. Early paper money was simply a written promise to pay a certain amount of gold or silver money. The paper money was valuable because it could be traded for gold or silver. Later, governments began printing paper money. In the 1900s most governments made paper money valuable on its own. It no longer stood for gold or silver.\n
"""

content = {
    "heading one": {
        "content": evolution_of_money,
        "image": "assets/images/science/science lab.png",
        "audio": "assets/audio/audio.mp3",
    },
    "heading two": {
        "content": evolution_of_money,
        "image": "assets/images/science/science lab.png",
        "audio": "assets/audio/audio.mp3",
    },
    "heading three": {
        "content": content_detail,
        "image": "assets/images/science/science lab.png",
        "audio": "assets/audio/audio.mp3",
    },
    "heading four": {
        "content": content_detail,
        "image": "assets/images/science/science lab.png",
        "audio": "assets/audio/audio.mp3",
    },
    "heading five": {
        "content": content_detail,
        "image": "assets/images/science/science lab.png",
        "audio": "assets/audio/audio.mp3",
    },
}

db = {
    "financial literacy": {
        "description": "Learn how to manage and use money effectively.",
        "image": "assets/images/financial literacy/financial literacy.png",
        "bg_color": "#ff9f52",

        "introduction to money": {
            "description": "Financial Literacy brought to you by Mara, a crypoto company and a financial coach.",

            "evolution of money": {
                "description": "How money has evolved over time in the financial world.",
                "content": content,
            },
            "importance of money": {
                "description": "Learn why money is important and why you should care.",
                "content": content,
            },
            "budgeting": {
                "description": "For better financial growth, budgeting is a key skill",
                "content": content,
            },
        },
        "blockchain": {
            "description": "Unit content description goes here Lorem ipsum congries mando good Unit content description goes here Lorem ipsum congries mando good",

            "introduction": {
                "description": "Sub topic Content description goes here",
                "content": blockchain,
            },
            "functions": {
                "description": "Sub topic Content description goes here",
                "content": content,
            },
            "introduction to bitcoin": {
                "description": "Sub topic Content description goes here",
                "content": content,
            },
            "getting started": {
                "description": "Sub topic Content description goes here",
                "content": content,
            },
        },
        "loans and savings": {
            "description": "Unit content description goes here Lorem ipsum congries mando good Unit content description goes here Lorem ipsum congries mando good",

            "first subtopic": {
                "description": "Content description goes here",
                "content": content,
            },
            "second subtopic": {
                "description": "Content description goes here",
                "content": content,
            },
            "third subtopic": {
                "description": "Content description goes here",
                "content": content,
            },
        },
    },
    "mathematics": {
        "description": "Learn how to use numbers and how to solve problems.",
        "bg_color": "#00a18d",
        "image": "assets/images/math/math solver.png",
    },

    "science": {
        "description": "Learn how to use scientific principles and methods.",
        "bg_color": "#efc059",
        "image": "assets/images/science/science lab.png",

        "human body": {
            "description": "The human body is a complex, highly organized structure made up of unique cells that work together to accomplish the specific functions necessary for sustaining life.",

            "reproductive health": {
                "description": "The reproductive system of an organism, also known as the genital system, is the biological system made up of all the anatomical organs involved in sexual reproduction.",
                "content": reproductive_system,
            },
            "heart": {
                "description": "The heart is a fist-sized organ that pumps blood throughout your body. It's the primary organ of your circulatory system.",
                "content": heart,
            },
            "digestive system": {
                "description": "The human digestive system consists of the gastrointestinal tract plus the accessory organs of digestion. Digestion involves the breakdown of food.",
                "content": digestive_system,
            },
        },
        "second science unit": {
            "description": "Unit content description goes here Lorem ipsum congries mando good Unit content description goes here Lorem ipsum congries mando good",

            "first subtopic": {
                "description": "Sub topic Content description goes here",
                "content": content,
            },
            "second subtopic": {
                "description": "Sub topic Content description goes here",
                "content": content,
            },
            "third subtopic": {
                "description": "Sub topic Content description goes here",
                "content": content,
            },
        },
        "third science unit": {
            "description": "Unit content description goes here Lorem ipsum congries mando good Unit content description goes here Lorem ipsum congries mando good",

            "first subtopic": {
                "description": "Content description goes here",
                "content": content,
            },
            "second subtopic": {
                "description": "Content description goes here",
                "content": content,
            },
            "third subtopic": {
                "description": "Content description goes here",
                "content": content,
            },
        },
    },
    "conservation": {
        "description": "Learn methods of conservation.",
        "bg_color": "#f66747",
        "image": "assets/images/conservation/conservation.png",

        "first conservation unit": {
            "description": "Unit content description goes here Lorem ipsum congries mando good Unit content description goes here Lorem ipsum congries mando good",

            "first subtopic": {
                "description": "Sub topic Content description goes here",
                "content": content,
            },
            "second subtopic": {
                "description": "Sub topic Content description goes here",
                "content": content,
            },
            "third subtopic": {
                "description": "Sub topic Content description goes here",
                "content": content,
            },
        },
        "second conservation unit": {
            "description": "Unit content description goes here Lorem ipsum congries mando good Unit content description goes here Lorem ipsum congries mando good",

            "first subtopic": {
                "description": "Sub topic Content description goes here",
                "content": content,
            },
            "second subtopic": {
                "description": "Sub topic Content description goes here",
                "content": content,
            },
            "third subtopic": {
                "description": "Sub topic Content description goes here",
                "content": content,
            },
        },
        "third conservation unit": {
            "description": "Unit content description goes here Lorem ipsum congries mando good Unit content description goes here Lorem ipsum congries mando good",

            "first subtopic": {
                "description": "Content description goes here",
                "content": content,
            },
            "second subtopic": {
                "description": "Content description goes here",
                "content": content,
            },
            "third subtopic": {
                "description": "Content description goes here",
                "content": content,
            },
        },
    },
}
