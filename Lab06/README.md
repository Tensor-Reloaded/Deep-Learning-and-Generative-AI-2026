# Lab06 · Reinforcement Learning

From learning action values to planning with a learned model: **Q-learning → DQN → AlphaGo Zero / AlphaZero → MuZero → ReBeL**.

## Materials from previous editions

The paper sequence below is preserved from [CARN Lab09 (2023)](https://github.com/Tensor-Reloaded/Advanced-Topics-in-Neural-Networks-Template-2023/tree/main/Lab09) and [CARN Lab07 (2025)](https://github.com/Tensor-Reloaded/Advanced-Topics-in-Neural-Networks-Template-2025/tree/main/Lab07). Use the paper table as the presentation entry point. A separate historical RL slide deck has not yet been identified.

All page numbers below are **1-based PDF viewer pages**, including title pages, not journal page numbers. Links jump to the first page of each range; if the browser ignores `#page=`, enter the page manually.

## Two-hour presentation order

| Minutes | Open | Activity / question |
|---|---|---|
| 0–15 | Board: agent–environment loop; [DQN 2013, pp. 2–3](https://arxiv.org/pdf/1312.5602#page=2) | A robot can take +1 now or a route to +10 later. Define state, action, transition, reward and policy. What if its battery level is missing from the state? |
| 15–30 | Board: Q-learning update below; [DQN 2013, p. 3](https://arxiv.org/pdf/1312.5602#page=3) | Q-learning and exploration. Do Exercise 1 below (5 minutes). |
| 30–50 | [DQN 2013 p. 5](https://arxiv.org/pdf/1312.5602#page=5), [DQN 2015 pp. 2 and 7](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf#page=2) | Replace the Q-table with a CNN. Trace one replay minibatch; contrast the 2013 algorithm with the 2015 target-network version. Why stack frames? |
| 50–80 | [AlphaGo Zero p. 2](https://augmentingcognition.com/assets/Silver2017a.pdf#page=2), [AlphaZero pp. 3–4](https://arxiv.org/pdf/1712.01815#page=3) | Follow self-play → MCTS visit counts → policy/value training → better search. Do Exercise 2 (5 minutes). Explain what generalizes from Go to chess and shogi. |
| 80–105 | [MuZero pp. 3–5](https://arxiv.org/pdf/1911.08265#page=3) | Trace representation h, dynamics g, prediction f through Figure 1. Identify reward/value/policy targets. Does the model need to reconstruct pixels? |
| 105–115 | [ReBeL pp. 1–2](https://arxiv.org/pdf/2007.13544#page=1) | Use Figure 1's modified rock–paper–scissors to show why hidden information changes search. Introduce public belief states; leave CFR details for further reading. |
| 115–120 | Comparison and exit questions below | Explain the difference between learning values, searching with known rules, and searching with learned dynamics. |

If discussion runs long, keep MuZero's Figure 1 and move the ReBeL discussion to further reading. This is a conceptual seminar and guided paper reading, not a reproduction of these large-scale training runs.

## Papers — direct links and projection guide

| Paper | Links | PDF pages / figures to discuss |
|---|---|---|
| **Playing Atari with Deep Reinforcement Learning** — Mnih et al., 2013 | [arXiv](https://arxiv.org/abs/1312.5602) · [PDF](https://arxiv.org/pdf/1312.5602) | [p. 2, Fig. 1](https://arxiv.org/pdf/1312.5602#page=2): Atari observations; [p. 3](https://arxiv.org/pdf/1312.5602#page=3): Bellman equation and TD loss; [p. 5, Algorithm 1](https://arxiv.org/pdf/1312.5602#page=5): replay and training; [p. 7, Figs. 2–3](https://arxiv.org/pdf/1312.5602#page=7): learning curves and predicted values. |
| **Human-level control through deep reinforcement learning** — Mnih et al., 2015 | [Nature / DOI](https://doi.org/10.1038/nature14236) · [author-hosted PDF](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf) | [p. 2, Fig. 1](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf#page=2): CNN → action values; [p. 7, Algorithm 1](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf#page=7): frozen target network, replay, and periodic parameter copy. This supplements the 2013 paper; do not attribute this exact algorithm to the earlier version. |
| **Mastering the game of Go without human knowledge (AlphaGo Zero)** — Silver et al., 2017 | [Nature / DOI](https://doi.org/10.1038/nature24270) · [PDF used in previous years](https://augmentingcognition.com/assets/Silver2017a.pdf) | [p. 2, Figs. 1–2 and Eq. 1](https://augmentingcognition.com/assets/Silver2017a.pdf#page=2): self-play, search, policy/value loss; [p. 3, Figs. 3–4](https://augmentingcognition.com/assets/Silver2017a.pdf#page=3): learning and architecture comparisons. |
| **Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm (AlphaZero)** — Silver et al., 2017 | [arXiv](https://arxiv.org/abs/1712.01815) · [PDF](https://arxiv.org/pdf/1712.01815) | [pp. 2–3, Eq. 1](https://arxiv.org/pdf/1712.01815#page=2): policy/value network, MCTS and self-play targets; [p. 4, Fig. 1](https://arxiv.org/pdf/1712.01815#page=4): chess, shogi and Go learning curves. Same general algorithm, separately trained instances for each game. |
| **Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model (MuZero)** — Schrittwieser et al., 2019 preprint / 2020 Nature | [arXiv](https://arxiv.org/abs/1911.08265) · [PDF](https://arxiv.org/pdf/1911.08265) | [p. 3, Fig. 1](https://arxiv.org/pdf/1911.08265#page=3): planning, acting and training; [p. 4, §3 and Eq. 1](https://arxiv.org/pdf/1911.08265#page=4): h/g/f and the unrolled loss; [p. 5, Fig. 2](https://arxiv.org/pdf/1911.08265#page=5): results. |
| **Combining Deep Reinforcement Learning and Search for Imperfect-Information Games (ReBeL)** — Brown et al., 2020 | [arXiv](https://arxiv.org/abs/2007.13544) · [PDF](https://arxiv.org/pdf/2007.13544) | [pp. 1–2, Fig. 1](https://arxiv.org/pdf/2007.13544#page=1): hidden-information counterexample; [p. 3](https://arxiv.org/pdf/2007.13544#page=3): public belief states; [p. 6, Algorithm 1](https://arxiv.org/pdf/2007.13544#page=6): optional self-play/search details. |

AlphaGo Zero and AlphaZero are distinct papers. For the two Nature articles above, the DOI and accessible PDF are supplied rather than an unverified arXiv equivalent.

## Board exercises

### 1. One Q-learning update

For one observed transition, let `Q(s,a)=2`, reward `r=1`, learning rate `α=0.1`, discount `γ=0.9`, and next-state action values `[3, 4]`.

$$y = r + \gamma(1-d)\max_{a'} Q(s',a')$$

$$Q(s,a) \leftarrow Q(s,a) + \alpha\big[y-Q(s,a)\big]$$

1. Compute the target, TD error and updated Q-value when `d=0` (the next state is not terminal).
2. Repeat when `d=1` (a true terminal state). Why must future value disappear?
3. In DQN, which network produces the target, which parameters receive gradients, and what does the replay buffer store?

Here `d` denotes a true environment termination, not merely a rollout cut short by a time limit.

### 2. Where do self-play training labels come from?

At one state, MCTS visits three legal moves `[10, 30, 60]` times. Use temperature `τ=1`. The policy head currently predicts `p=[0.2, 0.3, 0.5]`, the value head predicts `v=0.2`, and the player to move eventually wins (`z=+1`).

$$\ell = (z-v)^2 - \sum_a \pi_a \log p_a + c\lVert\theta\rVert^2$$

1. Compute the policy target `π` from visit counts and the value-loss term.
2. Which part of the loss trains each output? Where did each target come from?
3. What value target belongs to a position where the other player was to move? Is `π` a one-hot label for the move actually played?

## Compare the approaches

| Method | Learned outputs | Planning at action selection | Training signal |
|---|---|---|---|
| DQN | Q(s,a) for each discrete action | No explicit tree search; ε-greedy during exploration | Rewards and bootstrapped next-state values from replay |
| AlphaGo Zero / AlphaZero | Policy and value | MCTS using known game transitions | Search visit distribution and self-play game outcome |
| MuZero | Representation, latent dynamics, reward, policy, value | Search through learned latent dynamics | Observed rewards, search policy targets and value targets |
| ReBeL | Values and optionally policies over public belief states | Search accounting for hidden information; not ordinary perfect-information MCTS | Self-play plus game-solving targets over belief states |

**Exit questions:** Why is a Q-value not an action probability? Why does AlphaZero still need search? What does MuZero learn that AlphaZero is given? Why is knowing the rules insufficient for ordinary AlphaZero-style search in poker?

## Further viewing and source history

The paper sequence and videos are retained from [Lab09 (2023)](https://github.com/Tensor-Reloaded/Advanced-Topics-in-Neural-Networks-Template-2023/tree/main/Lab09) and [Lab07 (2025)](https://github.com/Tensor-Reloaded/Advanced-Topics-in-Neural-Networks-Template-2025/tree/main/Lab07).

- DQN discussions: [video 1](https://www.youtube.com/watch?v=rFwQDDbYTm4), [video 2](https://www.youtube.com/watch?v=nOBm4aYEYR4).
- [AlphaZero discussion](https://www.youtube.com/watch?v=O1b0cbgpRBw).
- [MuZero discussion](https://www.youtube.com/watch?v=We20YSAJZSE).
- [ReBeL discussion](https://www.youtube.com/watch?v=BhUWvQmLzSk).

These are optional follow-up videos, not videos to play in full during the seminar.
