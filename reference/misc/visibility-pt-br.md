---
doc_id: "mta-wiki:12812"
title: "PT-BR/Visibility"
source_title: "Visibility/PT-BR"
source_url: "https://wiki.multitheftauto.com/wiki/Visibility/PT-BR"
revision_id: 69095
language: "en"
categories: []
generated_at: "2026-07-26T16:07:49.425839+00:00"
---

# PT-BR/Visibility

O sistema de visibilidade para marker e blips funciona pela seguinte regra: se algo é visível para um determinado elemento, ele também é visível para todos os filhos desse elemento. Além disso, tudo fica visível para o elemento raiz por padrão.

Isso significa que, se você quiser fazer, por exemplo, um blip visível apenas para alguns jogadores específicos, você precisa fazer duas coisas:

- Faça o blip ficar invisível para o elemento root (todos), usando [setElementVisibleTo](mta://scripting/server/functions/setelementvisibleto.md). Agora nenhum jogador está vendo o blip.

- Faça o blip ficar visível para os jogadores que forem especificados na função usada acima.

A mesma coisa pode ser feita para markers.

Dica: Se você deseja que apenas algo seja visível para determinados jogadores, a coisa mais eficiente e com menos erros é, quando criar o elemento em vez da visibilidade padrão do root, defina isto para resourceRoot (nenhum jogador verá pois nenhum jogador é filho de resourceRoot) e então use [setElementVisibleTo](mta://scripting/server/functions/setelementvisibleto.md) nos jogadores especificados. Caso contrário, há uma chance de que os jogadores vejam o blip por uma fração de segundo, pois o blip é criado, mas depois destruído.

Isso é ruim (chance de ser visto no minimapa por cerca de 50ms):

```
a = createBlip(0, 0, 0, 41)
setElementVisibleTo(a, root, false)
setElementVisibleTo(a, algumJogador, true)
```

Já a seguinte forma é bem mais adequada:

```
a = createBlip(0, 0, 0, 41, 1, 2, 3, 4, 5, 6, 9999, resourceRoot)
setElementVisibleTo(a, algumJogador, true)
```
