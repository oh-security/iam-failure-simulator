IAM Failure Simulator
====================

IAM Failure Simulator is a portfolio project designed to explain how IAM misconfigurations can evolve into real security incidents over time.

Instead of focusing on detection accuracy, this tool focuses on explainability and decision-making:
why a small IAM mistake becomes dangerous, and how that risk unfolds as a story.

This project is intentionally scoped for clarity and communication, not for production deployment.


Why this project exists
----------------------

IAM is one of the most common root causes of cloud security incidents.
In many cases, the problem is not technical complexity, but the lack of clear explanation before an incident happens.

As someone with a sales background working closely with engineers and security teams,
I observed that security often fails at the communication layer.

This tool was built to demonstrate how IAM risks can be explained clearly to both technical
and non-technical stakeholders, enabling better decisions before incidents occur.


What this tool does
-------------------

- Models IAM misconfigurations as time-based failure scenarios
- Explains how permissions, principals, and policies interact over time
- Focuses on "how it becomes an incident" rather than just flagging issues
- Demonstrates explainable security design using Python and AWS IAM concepts

This is not a detection tool.
It is an explanation and simulation tool.


Design principles
-----------------

- Explainability over detection accuracy
- Decision-making support over alert generation
- Simple structure that prioritizes intent and readability
- Designed as a learning and portfolio artifact, not a production system


Project structure
-----------------

src/
  Core logic for IAM failure simulation

rules/
  IAM misconfiguration and failure scenario definitions

examples/
  Example scenarios and reference outputs (optional / future use)

simulate.py
  Entry point for running simulations

requirements.txt
  Python dependencies

README.md
  Project overview and design intent


Technology
----------

- Python
- AWS IAM
- boto3

Future extensions may include CloudTrail-based action mapping and managed policy expansion,
but these are intentionally out of scope for the current version.


Who this project is for
-----------------------

- Security Engineers (Junior to Mid)
- Solutions Engineers / Architects
- Cloud and Platform Security roles
- Technical Sales and Security Advisors

Especially relevant for roles that require explaining security risks clearly,
not just implementing controls.


About the author
----------------

This project was created as part of a career transition from sales to security and cloud-related roles.

The focus is on combining technical understanding with clear communication,
demonstrating how security risks can be explained as stories that support better decisions.


Status
------

This project is intentionally not production-ready.
It prioritizes structure, intent, and explainability over full implementation.

That choice reflects real-world security work,
where understanding and communicating risk is often as important as building detection systems.
