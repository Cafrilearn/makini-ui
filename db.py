content_detail = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. \n
Kadim Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. \n
Humeai Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n
"""

parts_of_heart = """
The heart is made up of four different blood-filled areas, and each of these areas is called a chamber. There are two chambers on each side of the heart. One chamber is on the top and one chamber is on the bottom. The two chambers on top are called the atria
If you're talking only about one, call it an atrium. The atria are the chambers that fill with the blood returning to the heart from the body and lungs. The heart has a left atrium and a right atrium.

The two chambers on the bottom are called the ventricles.
The heart has a left ventricle and a right ventricle. Their job is to squirt out the blood to the body and lungs.
Running down the middle of the heart is a thick wall of muscle called the septum he septum's job is to separate the left side and the right side of the heart.
The atria and ventricles work as a team.
 the atria fill with blood, then dump it into the ventricles. 
The ventricles then squeeze, pumping blood out of the heart.
While the ventricles are squeezing, the atria refill and get ready for the next contraction. 

So when the blood gets pumped, how does it know which way to go?


Well, your blood relies on four special valves inside the heart. A valve lets something in and keeps it there by closing think of walking through a door. 
The door shuts behind you and keeps you from going backward.
These valves prevent the blood from flowing backward and guide the flow of blood
"""

intro_heart = """
We see and hear about hearts everywhere. A long time ago, people even thought that their emotions came from their hearts, maybe because the heart beats faster when a person is scared or excited. Now we know that emotions come from the brain, and in this case, the brain tells the heart to speed up. So what's the heart up to, then? How does it keep busy? What does it look like? Let's find out.

The Heart Is a Muscle
Your heart is really a muscle.
It's located a little to the left of the middle of your chest.s about the size of your fist. 
There are lots of muscles all over your body.
Muscles are in your arms, in your legs, in your back, even in your behind.
"""

reproductive_system = {
    "male reproductive system": {
        "content": content_detail,
        "image": "assets/images/science/science lab.png",
    },
    "female reproductive system": {
        "content": content_detail,
        "image": "assets/images/science/science lab.png",
    },
}

heart = {
    "introduction": {
        "content": intro_heart,
        "image": "",
    },
    "parts of the heart": {
        "content": parts_of_heart,
        "image": "assets/images/science/parts of heart.jpg",
    },
    "what it does": {
        "content": content_detail,
        "image": "assets/images/science/science lab.png",
    },
    "beating of the heart": {
        "content": content_detail,
        "image": "assets/images/science/science lab.png",
    },
    "blood circulation": {
        'content': content_detail,
        "image": "assets/images/science/science lab.png",
    }
}

digestive_system = {
    "introduction": {
        "content": content_detail,
        "image": "assets/images/science/science lab.png",
    },
    "mouth": {
        "content": content_detail,
        "image": "assets/images/science/science lab.png",
    },
    "small intestines": {
        "content": content_detail,
        "image": "assets/images/science/science lab.png",
    },
    "stomach": {
        "content": content_detail,
        "image": "assets/images/science/science lab.png",
    },
    "large intestines": {
        "content": content_detail,
        "image": "assets/images/science/science lab.png",
    },
}

content = {
    "wonder heading": {
        "content": content_detail,
        "image": "assets/images/science/science lab.png",
    },
    "heading two": {
        "content": content_detail,
        "image": "assets/images/science/science lab.png",
    },
    "heading three": {
        "content": content_detail,
        "image": "assets/images/science/science lab.png",
    },
    "heading four": {
        "content": content_detail,
        "image": "assets/images/science/science lab.png",
    },
    "heading five": {
        "content": content_detail,
        "image": "assets/images/science/science lab.png",
    },
}

db = {
    "financial literacy": {
        "description": "Learn how to manage and use money effectively.",
        "image": "assets/images/financial literacy/financial literacy.png",
        "bg_color": "#ff9f52",

        "first financial unit": {
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
        "second financial unit": {
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
        "third financial unit": {
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
