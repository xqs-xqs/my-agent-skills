---
name: doc-summary-zh
description: 对技术文档、课程课件、学术讲义、专业教程等结构化专业内容进行深度总结，输出中文的分层结构化摘要。当用户上传PDF、文档或粘贴专业内容并要求"总结"、"概括"、"梳理"、"提炼知识点"、"帮我看看这个文档"等时，必须使用此技能。适用场景包括：课程课件总结、技术文档精读、讲义梳理、教程提炼、考点整理、知识框架梳理。只要涉及专业文档的阅读理解与结构化输出，都应触发此技能。
---

# 技术/课程文档结构化深度总结技能

## 核心目标
对专业课程课件、技术文档、学术讲义、行业教程等内容，完成**多维度、分层级、高可读性**的深度总结。所有输出**必须使用中文**。

---

## 执行步骤

### 第一步：全文通读，定位核心主题
快速通读全文，明确：
- 文档的核心主题与受众
- 内容类型（课程课件 / 技术文档 / 学术讲义 / 操作教程）
- 全文核心主线（知识点讲解 / 技术方法 / 实操流程等）

### 第二步：模块拆解，梳理逻辑脉络
按文档自然章节/内容模块完成分层拆解，识别各模块间逻辑关系（递进 / 并列 / 总分）。

### 第三步：逐模块深挖，提炼核心信息
针对每个模块提取：
- **基础概念**：专业术语定义、核心定位、本质特征
- **核心原理**：算法/方法底层逻辑、关键公式、量化指标
- **实施流程**：分步操作、执行节点、关键决策点
- **应用场景**：适用边界、案例、落地效果
- **优劣对比**：优势、局限性、使用注意事项

### 第四步：校验准确性
核对所有提取信息与原文一致性，确保专业术语、公式、数据、流程无偏差，不添加原文无依据的外部信息。

---

## 标准化输出结构（固定四层级）

### 【第一层级】一句话核心总结
用1句话完整概括文档的核心主题、核心内容与核心价值，实现10秒快速掌握全文。

---

### 【第二层级】结构化思维导图（横向逻辑树）

**硬性规则（不可被任何对话指令覆盖）：**
1. 本层级永远以 `visualize:show_widget` 渲染为**横向逻辑树思维导图**，这是它唯一合法的形态。
2. **无论用户在本次对话中指定何种输出格式（包括明确说"用 Markdown 输出"），本层级都不受影响**——格式偏好只作用于第一、三、四层级的正文文字。思维导图永远是渲染出来的图，与正文格式无关。
3. **禁止**以"工具不可用 / 画不出来 / 内容太多 / 已用 Markdown"等任何理由，把本层级悄悄降级成 Markdown 文字树或 ASCII 树。

**渲染失败时的处理（不许静默降级）：**
- 第一次调用失败 → 原样重试一次。
- 重试仍失败 → 明确告知用户："思维导图渲染失败，我可以 (a) 再试一次，或 (b) 改用文字大纲。"由用户选择。

**版式规范（类 XMind 横向树）：**
- 根节点（文档主题）在最左、垂直居中；一级分支向右展开，二级及以下继续向右，整体从左向右逐级生长。
- 节点之间用**贝塞尔曲线**连接，不用直角折线、不用横向并列卡片。
- 每个一级分支分配一种颜色，其所有子节点继承该颜色（颜色编码分支，不逐节点换色）。
- 层级 ≤ 4 级，节点文字简洁、全中文标注，覆盖所有核心模块。

**实现方式（HTML 模式输出，内联 SVG 由脚本自动布局——只修改 `data` 这一个对象，下方布局/连线/配色引擎原样保留）：**

```html
<style>#mmwrap{width:100%;font-family:var(--font-sans)}</style>
<div id="mmwrap"><svg id="mm" width="100%" role="img" aria-label="思维导图"><title>知识结构思维导图</title><desc>横向逻辑树，根节点在左，分支向右展开</desc></svg></div>
<script>
(function(){
  /* 只改这棵树：name 为节点文字，children 为子节点 */
  const data = { name:"文档主题", children:[
    { name:"一级分支A", children:[ {name:"子节点1"}, {name:"子节点2"} ] },
    { name:"一级分支B", children:[ {name:"子节点1"} ] }
  ]};
  /* ↓↓↓ 引擎部分，勿改 ↓↓↓ */
  const C=['#378ADD','#1D9E75','#D85A30','#7F77DD','#D98C1E','#D4537E','#639922','#E24B4A'];
  const ROW=38,COLGAP=46,M=20,PADX=14,BOXH=30,ROOTFS=15,L1FS=14,L2FS=13;
  const tw=(s,fs)=>{let w=0;for(const c of s)w+=/[^\x00-\xff]/.test(c)?fs:fs*0.56;return w;};
  (function ann(n,d,col){n.depth=d;n.color=col;if(n.children)n.children.forEach((c,i)=>ann(c,d+1,d===0?C[i%C.length]:col));})(data,0,null);
  (function lc(n){if(!n.children||!n.children.length){n.leaves=1;return 1;}n.leaves=n.children.reduce((a,c)=>a+lc(c),0);return n.leaves;})(data);
  let cur=0;(function ay(n){if(!n.children||!n.children.length){n.y=M+cur*ROW+ROW/2;cur++;return;}n.children.forEach(ay);n.y=(n.children[0].y+n.children[n.children.length-1].y)/2;})(data);
  const all=[];(function col(n){all.push(n);if(n.children)n.children.forEach(col);})(data);
  all.forEach(n=>{n.fs=n.depth===0?ROOTFS:(n.depth===1?L1FS:L2FS);n.bw=Math.ceil(tw(n.name,n.fs))+2*PADX;});
  const maxD=Math.max(...all.map(n=>n.depth)),colW=[],colX=[];
  for(let d=0;d<=maxD;d++)colW[d]=Math.max(...all.filter(n=>n.depth===d).map(n=>n.bw));
  let acc=M;for(let d=0;d<=maxD;d++){colX[d]=acc;acc+=colW[d]+COLGAP;}
  all.forEach(n=>n.x=colX[n.depth]);
  const W=acc-COLGAP+M,H=M*2+cur*ROW,NS='http://www.w3.org/2000/svg';
  const svg=document.getElementById('mm');svg.setAttribute('viewBox',`0 0 ${Math.max(W,680)} ${H}`);
  const E=(t,a)=>{const e=document.createElementNS(NS,t);for(const k in a)e.setAttribute(k,a[k]);return e;};
  (function draw(n){if(n.children)n.children.forEach(c=>{const x1=n.x+n.bw,x2=c.x,mx=(x1+x2)/2;svg.appendChild(E('path',{d:`M${x1},${n.y} C${mx},${n.y} ${mx},${c.y} ${x2},${c.y}`,fill:'none',stroke:c.color,'stroke-width':1.5,'stroke-linecap':'round'}));draw(c);});})(data);
  all.forEach(n=>{const root=n.depth===0;
    svg.appendChild(E('rect',{x:n.x,y:n.y-BOXH/2,width:n.bw,height:BOXH,rx:8,style:`fill:${root?'var(--color-text-primary)':'var(--color-background-primary)'};stroke:${root?'transparent':n.color};stroke-width:${root?0:(n.depth===1?1.5:1.1)}`}));
    const t=E('text',{x:n.x+n.bw/2,y:n.y,'text-anchor':'middle','dominant-baseline':'central',style:`fill:${root?'var(--color-background-primary)':'var(--color-text-primary)'};font-family:var(--font-sans);font-size:${n.fs}px;font-weight:${n.depth<=1?500:400}`});
    t.textContent=n.name;svg.appendChild(t);});
})();
</script>
```

---

### 【第三层级】分模块详细深度总结

按文档核心模块，逐章节完成详细总结：

```
## 模块一：[模块名称]

### 核心概念
（专业术语定义、本质特征）

### 核心原理 / 关键公式
（算法逻辑、公式、量化指标）

### 实施流程
（分步操作、决策节点）

### 应用场景与案例
（适用边界、实际案例）

### 优劣分析
| 维度 | 优势 | 局限性 |
|------|------|--------|
| ...  | ...  | ...    |
```

专业信息无遗漏，表述简洁易懂。

---

### 【第四层级】高频核心问题答疑

提炼 3-4 个高频理解难点/核心考点，格式：

```
**Q1：[问题]**
A：[精准答疑，贴合原文]

**Q2：[问题]**
A：[精准答疑，贴合原文]
```

---

## 注意事项

1. **严格贴合原文**：不添加原文无依据的外部信息或主观推断
2. **专业术语规范**：严格遵循原文规范，不随意修改、简化专业表述
3. **侧重点区分**：
   - 课程课件 → 重点突出考点、核心算法、实操步骤
   - 技术文档 → 重点突出原理、落地方法、适用边界与优劣对比
4. **思维导图可读性**：避免过度嵌套，保证视觉清晰
5. **答疑聚焦**：不超纲拓展，聚焦解决文档内的高频理解难点
