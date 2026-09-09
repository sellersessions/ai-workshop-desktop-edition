# Amazon sub‑agents into a single “from product idea to launch” workflow

Yes, you can chain your Amazon sub‑agents into a single “from product idea to launch” workflow, but you do it at the *prompt / agent design* level rather than wiring agents together like Zapier.

Below is a concrete, non‑code way to do it using the eight agents in your README and a simple “conductor” pattern.

---

## Two basic patterns

1. **Manual chaining (simplest)**
    - You stay in one Claude chat and run agents in sequence with clear prompts, reusing context each time.
    - Example sequence:
        1. “Use the **trend researcher** agent to find three promising product ideas in [category] for Amazon UK.”
        2. “Using the best opportunity above, use the **reddit community builder** agent to find top complaints and desires for this product type.”
        3. “Now, using that insight, use the **content creator** agent to draft a listing (title, bullets, description) for the chosen product.”
        4. “Use the **growth hacker** agent to create a 30‑day launch plan for this exact product.”
        5. “Use the **tiktok strategist** agent to propose 10 TikTok hooks based on this launch plan.”
        6. “Use the **feedback synthesiser** agent to analyse these example competitor reviews for this niche: [paste reviews].”
        7. “Use the **analytics reporter** agent to define the key KPIs and a simple weekly reporting layout for this product.”
        8. “Use the **support responder** agent to create five FAQ entries and five canned replies to typical issues for this product.”
    
    Because the agents remember context for the whole conversation, you can keep reusing the same product, customer avatar, objections, and so on, without restating everything every time.
    
2. **Conductor agent (more automated)**
    - You add one more custom agent whose sole job is: “Run the whole Amazon workflow and explicitly call the other eight agents in order.”
    - In its instructions, you describe the pipeline and tell it when and how to switch “hats”.

---

## Example conductor agent design

Create a new agent file, for example [`amazon-product-pipeline.md`](http://amazon-product-pipeline.md) in your `~/.claude/agents/` folder.

In plain English (no code required), you’d give it instructions along these lines:

- **Goal**
    - Take an Amazon seller from zero product to a launch‑ready listing, content plan, and support assets using the existing eight sub‑agents.
- **Workflow you must follow (steps):**
    1. Use the **trend researcher** agent to find three to five product opportunities in the user’s chosen category and marketplace. Ask the user to confirm which opportunity to pursue.
    2. Once confirmed, use the **reddit community builder** agent to pull key pains, desires, and language for that product audience.
    3. Use the **content creator** agent to draft an Amazon‑optimised listing (title, bullets, description, A+ outline) keyed to those pains and desires.
    4. Use the **growth hacker** agent to design a 30‑day launch plan for that specific product and listing.
    5. Use the **tiktok strategist** agent to create a TikTok content calendar that supports the launch plan.
    6. Ask the user for competitor reviews or sample reviews; then use the **feedback synthesiser** agent to extract insights and refine the listing and launch plan.
    7. Use the **analytics reporter** agent to define a simple dashboard/KPI report the seller should update weekly.
    8. Use the **support responder** agent to:
        - Generate FAQs for the listing.
        - Draft canned reply templates for the most likely issues uncovered in previous steps.
- **Interaction rules**
    - Always show which step you are in (for example, “Step 3/8 – Listing creation with Content Creator agent”).
    - Before moving to the next step, briefly summarise outputs and ask the user if they want to tweak or proceed.
    - Reuse previous information instead of asking the user to repeat it.

Then, when you want the full chain, you just say in Claude:

> “Use the amazon-product-pipeline agent to take me from product research to launch. My category is: [X], my marketplace is: [Y]. Assume I am a private‑label seller starting from scratch.”
> 

The conductor agent then internally invokes the relevant sub‑agents step by step, but from your point of view it’s one smooth conversation.

---

## How to prototype this today (no re‑wiring)

If you want to try it right now without editing agent files yet:

1. Start a new Claude chat.
2. Paste in a short instruction block like:
    
    > “In this conversation, behave as a conductor for my Amazon agents. Follow this sequence:
    > 
    > 1. Use the trend researcher agent…
    > 2. Use the reddit community builder agent…
    > 3. Use the content creator agent…
    > 4. Use the growth hacker agent…
    > 5. Use the tiktok strategist agent…
    > 6. Use the feedback synthesiser agent…
    > 7. Use the analytics reporter agent…
    > 8. Use the support responder agent…
    >     
    >     At each step, clearly label what you’re doing and carry forward context from earlier steps.”
    >     
3. Then say: “Start from Step 1 for the [niche] in [market].”

This lets you experiment with the flow and wording before you bake it into a dedicated conductor agent file.

---

## Mapping your eight agents into the chain

| Stage in journey | Agent to use | What you get out of it |
| --- | --- | --- |
| 1. Find product idea | trend researcher | Shortlist of product opportunities and rationale |
| 2. Deep customer insight | reddit community builder | Real pain points, language, objections |
| 3. Listing creation | content creator | Amazon‑ready copy: title, bullets, descriptions, A+ skeleton |
| 4. Launch strategy | growth hacker | 30‑day launch plan with phases and key actions |
| 5. Social engine | tiktok strategist | TikTok hooks, angles, and posting schedule aligned to the launch plan |
| 6. Review‑driven refining | feedback synthesiser | Clear list of must‑fix issues and differentiators from customer review analysis |
| 7. Measurement layer | analytics reporter | KPIs, basic dashboard/report template for tracking launch and ongoing performance |
| 8. Post‑purchase support | support responder | FAQs and email/message templates to handle common situations and protect reviews |

If you’d like, the next step can be: paste one of your existing Amazon agent `.md` files, plus a niche you care about, and a conductor‑agent file can be drafted for you line by line in a way that you can just drop into `~/.claude/agents/`.

1. [https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/24742573/e340a5f2-3647-4177-b8e3-f33627e6fbb6/README.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/24742573/e340a5f2-3647-4177-b8e3-f33627e6fbb6/README.md)