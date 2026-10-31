# 计算机网络 第 6 章：TCP 拥塞控制

【第 1 页】什么是拥塞
多个发送方向网络注入的数据超过链路或路由器缓存的承载能力时，出现丢包与排队时延激增，称为拥塞。拥塞控制关注的是"网络"，流量控制关注的是"接收方"。

【第 2 页】拥塞窗口 cwnd
发送方维护拥塞窗口 cwnd，实际发送窗口 = min(cwnd, rwnd)。发送速率约为 cwnd / RTT。

【第 3 页】慢启动
连接建立时 cwnd = 1 MSS，每收到一个 ACK，cwnd 增加 1 MSS，因此每个 RTT cwnd 翻倍（指数增长），直到达到慢启动阈值 ssthresh。

【第 4 页】拥塞避免
cwnd ≥ ssthresh 后进入拥塞避免，每个 RTT cwnd 只增加 1 MSS（线性增长，加法增大 AI）。

【第 5 页】丢包检测与反应
超时（RTO）：ssthresh = cwnd/2，cwnd = 1 MSS，重新慢启动。
三个重复 ACK：说明网络仍能传递部分报文，执行快重传，立即重传丢失报文段，不等待超时。

【第 6 页】快恢复（TCP Reno）
收到 3 个重复 ACK 后：ssthresh = cwnd/2，cwnd = ssthresh + 3 MSS，之后每收到一个重复 ACK cwnd 加 1 MSS；收到新 ACK 后 cwnd = ssthresh，进入拥塞避免。Tahoe 没有快恢复，无论哪种丢包都把 cwnd 置为 1。

【第 7 页】AIMD 与公平性
加法增大、乘法减小（AIMD）使竞争同一瓶颈链路的多条 TCP 流的吞吐量收敛到公平分配。但 RTT 较短的流增长更快，会获得更多带宽（RTT 不公平）。

【第 8 页】CUBIC
Linux 默认算法。窗口增长是距上次丢包时间的三次函数：W(t) = C(t − K)^3 + W_max，K = ∛(W_max·β/C)。在 W_max 附近增长平缓、远离时快速探测；增长与 RTT 无关，改善了高带宽长时延网络中的利用率与 RTT 公平性。

【第 9 页】BBR
Google 提出，基于模型而非丢包：持续估计瓶颈带宽 BtlBw 与最小往返时延 RTprop，使在途数据量约等于 BDP = BtlBw × RTprop，并按估计带宽调节发送速率（pacing）。优点：在浅缓存/有随机丢包链路上吞吐高、排队时延低；局限：与 Reno/CUBIC 共存时可能不公平，BBRv1 在深缓存下会造成较多重传。

【第 10 页】ECN
显式拥塞通知：路由器在 IP 头标记 CE 位而不是丢包，接收方通过 TCP 头的 ECE 回显，发送方减小 cwnd 并置 CWR。需要两端与路径设备均支持。

【第 11 页】小结与考点
慢启动/拥塞避免/快重传/快恢复的状态转移与 cwnd 计算是必考题；能区分 Tahoe 与 Reno；理解 AIMD 的公平性论证；了解 CUBIC 与 BBR 的设计出发点。
