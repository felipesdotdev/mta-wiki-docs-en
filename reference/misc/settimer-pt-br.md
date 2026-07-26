---
doc_id: "mta-wiki:12474"
title: "PT-BR/SetTimer"
source_title: "SetTimer/PT-BR"
source_url: "https://wiki.multitheftauto.com/wiki/SetTimer/PT-BR"
revision_id: 67194
language: "en"
categories: []
generated_at: "2026-07-26T16:07:35.880465+00:00"
---

# PT-BR/SetTimer

| [[{{{image}}}\|link=\|]] | Nota Importante: A velocidade na qual um timer em client-side é executado pode não ser totalmente confiável se este client estiver modificando maliciosamente a velocidade do sistema operacional, os timers poderão ser executados muito mais rápido ou mais devagar. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Nota Importante: Usando o código abaixo pode haver problemas na performance. Ao invés disso, use onClientPreRender . setTimer(Funcao, 0, 0) |
| --- | --- |
|  |  |

Esta função permite você acionar uma função depois de um número de milissegundos estiver decorrido. Você pode executar funções que tenham um nome sendo uma variável, uma função anônima, ou uma função do MTA (tipo [setElementModel](mta://scripting/shared/functions/setelementmodel.md)). Por exemplo, você pode definir um timer para *spawnar* um jogador depois de alguns segundos.

A partir que o timer termina suas execuções, ele deixa de existir.

O invervalo mínimo aceito é **0ms**.

O MTA garante que o timer será acionado após pelo menos o intervalo especificado. O funcionamento do timer está vinculado à taxa de quadros (lado do servidor e lado do cliente). Todos os timers finalizados são acionados em um único ponto em cada quadro(frame). Isto significa que se, por exemplo, o jogador está rodando a 30 fps, então dois timers criados para acionar suas funções em 100ms e 110ms provavelmente ocorrerão durante o mesmo frame, pois a diferença de tempo entre os dois temporizadores (10 ms) é menor que a metade do comprimento do quadro (33 ms). Como na maioria dos timers fornecidos por outras linguagens de programação, você não deve confiar no disparo do cronômetro em um ponto exato no futuro.

## Sintaxe

```
timer setTimer ( function theFunction, int timeInterval, int timesToExecute [, var arguments... ] )
```

**Sintaxe POO(OOP)** [Não entendeu o que significa isso?](mta://tutorials/oop-introduction.md)

**Método**: *[Timer](mta://reference/misc/timer.md)(...)*

### Argumentos Necessários

- **theFunction:** A função que o timer vai executar quando estiver decorrido o invervalo definido.

|  | Nota: A variável global escondida ( sourceTimer ) da função que foi executada pelo timer contém a atual userdata deste timer que está em execução. |
| --- | --- |
|  |  |

- **timeInterval:** Número de milissegundos que deve decorrer antes da função especificada ser exeuctada. [o mínimo é 50 (0 a partir da versão 1.5.6 r16715); 1000 milissegundos = 1 segundo]

- **timerToExecute:** O número de vezes que o timer deve executar. **0** significa que o timer vai ser repetido infinitas vezes.

### Argumentos Opcionais

*NOTA:* Ao usar argumentos opcionais, pode ser necessário fornecer todos os argumentos anteriores ao que você deseja usar. Para obter mais informações sobre argumentos opcionais, consulte [Argumentos Opcionais](https://wiki.multitheftauto.com/wiki/BR/Argumentos_Opcionais).

- **arguments:** Qualquer argumento que você deseja passar para a função podem ser listados depois do argumento *timesToExecute*. Note que qualquer tabela que você deseja passar será clonada, enquanto que referências de metatabelas e funções passadas na tabela serão perdidas. As alterações feitas na tabela original antes que a função seja chamada não serão transferidas.

### Retorna

Retorna um [timer](mta://reference/misc/timer.md) se for criado com sucesso, *false* se os argumentos são inválidos ou se o timer não pôde ser definido.

## Exemplos

Click to collapse [-]
Exemplo 1

Este exemplo vai exibir no chat algum texto depois de um pequeno delay.

```
-- defina a função que vai ser executada
function chatAtrasado ( text )
	outputChatBox ( "Texto atrasado: " .. text )
end

-- Defina um timer e então a função será executada depois de 1 segundo
setTimer ( chatAtrasado, 1000, 1, "Olá Brasil!" )
```

1 segundo depois que a linha acima for executada, o texto *Texto atrasado: Olá Brasil!* vai ser exibido no chat.

Click to collapse [-]
Exemplo 2

Este exemplo aninha uma função inteira dentro de um timer. Isso é bom para coisas como definir variáveis sem precisar chamar uma função fora do seu bloco de código.

```
function funcaoPrincipal()
        outputChatBox ("Texto agora!")
	setTimer ( function()
		outputChatBox ( "Texto depois de 5 segundos depois do último!" )
	end, 5000, 1 )
end

funcaoPrincipal() -- execute a função
```

Click to collapse [-]
Exemplo 3

Este exemplo deve enviar no chat global algo sobre a morte de um jogador em um tempo aleatório. Eu usei [math.round](https://wiki.multitheftauto.com/wiki/Math.round) neste exemplo para se tornar mais útil.

```
function math.round(number, decimals, method) -- math.round, função útil obtida de wiki: https://wiki.multitheftauto.com/wiki/Math.round
    decimals = decimals or 0
    local factor = 10 ^ decimals
    if (method == "ceil" or method == "floor") then return math[method](number * factor) / factor
    else return tonumber(("%."..decimals.."f"):format(number)) end
end

function quandoMorto()
	local delay = math.random(500, 5000) -- 0.5s até 5s de delay
	setTimer(function(thePlayer) -- Inicia o timer
		local whoDied = "Someone" -- Caso o nome não seja obtido, Someone será usado
		if isElement(thePlayer) then -- Isto checa se o elemento thePlayer ainda existe (que significa que o thePlayer não desconectou ainda)
			whoDied = getPlayerName(thePlayer) -- Aqui obtemos o nome do jogador
		end
		outputChatBox(whoDied.." #FF0000morreu #FFFFFF"..math.round(delay/1000, 1).." segundos atrás.", root, 255, 175, 0, true) -- Isto vai exibir para todos no servidor que aquele thePlayer (ou alguém) morreu X segundos atrás.
	end
	delay, 1, source) -- O source no final é um argumento para a função que fizemos antes, você não pode usar source diretamente pois ele não estaria definido mais
end
addEventHandler("onPlayerWasted", root, quandoMorto) -- Executado a cada vez que alguém morre
```

## Veja também

- [addDebugHook](mta://scripting/shared/functions/adddebughook.md)

- [debugSleep](mta://scripting/shared/functions/debugsleep.md)

- [decodeString](mta://scripting/shared/functions/decodestring.md)

- [encodeString](mta://scripting/shared/functions/encodestring.md)

- [fromJSON](mta://scripting/shared/functions/fromjson.md)

- [generateKeyPair](mta://scripting/shared/functions/generatekeypair.md)

- [getColorFromString](mta://scripting/shared/functions/getcolorfromstring.md)

- [getDevelopmentMode](mta://scripting/shared/functions/getdevelopmentmode.md)

- [getDistanceBetweenPoints2D](mta://scripting/shared/functions/getdistancebetweenpoints2d.md)

- [getDistanceBetweenPoints3D](mta://scripting/shared/functions/getdistancebetweenpoints3d.md)

- [getEasingValue](mta://scripting/shared/functions/geteasingvalue.md)

- [getNetworkStats](mta://scripting/shared/functions/getnetworkstats.md)

- [getNetworkUsageData](mta://scripting/shared/functions/getnetworkusagedata.md)

- [getPerformanceStats](mta://scripting/shared/functions/getperformancestats.md)

- [getRealTime](mta://scripting/shared/functions/getrealtime.md)

- [getTickCount](mta://scripting/shared/functions/gettickcount.md)

- [getTimerDetails](mta://scripting/shared/functions/gettimerdetails.md)

- [getTimers](mta://scripting/shared/functions/gettimers.md)

- [getFPSLimit](mta://scripting/shared/functions/getfpslimit.md)

- [getUserdataType](mta://scripting/shared/functions/getuserdatatype.md)

- [getVersion](mta://scripting/shared/functions/getversion.md)

- [gettok](mta://scripting/shared/functions/gettok.md)

- [isTransferBoxVisible](mta://scripting/shared/functions/istransferboxvisible.md)

- [setTransferBoxVisible](mta://scripting/shared/functions/settransferboxvisible.md)

- [hash](mta://scripting/shared/functions/hash.md)

- [inspect](mta://scripting/shared/functions/inspect.md)

- [interpolateBetween](mta://scripting/shared/functions/interpolatebetween.md)

- [iprint](mta://scripting/shared/functions/iprint.md)

- [isOOPEnabled](mta://scripting/shared/functions/isoopenabled.md)

- [isTimer](mta://scripting/shared/functions/istimer.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22701](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22701):

- [isTimerPaused](mta://scripting/shared/functions/istimerpaused.md)

- [setTimerPaused](mta://scripting/shared/functions/settimerpaused.md)

- [killTimer](mta://scripting/shared/functions/killtimer.md)

- [md5](mta://scripting/shared/functions/md5.md)

- [passwordHash](mta://scripting/shared/functions/passwordhash.md)

- [passwordVerify](mta://scripting/shared/functions/passwordverify.md)

- [pregFind](mta://scripting/shared/functions/pregfind.md)

- [pregMatch](mta://scripting/shared/functions/pregmatch.md)

- [pregReplace](mta://scripting/shared/functions/pregreplace.md)

- [removeDebugHook](mta://scripting/shared/functions/removedebughook.md)

- [resetTimer](mta://scripting/shared/functions/resettimer.md)

- [setDevelopmentMode](mta://scripting/shared/functions/setdevelopmentmode.md)

- [setFPSLimit](mta://scripting/shared/functions/setfpslimit.md)

- [setTimer](mta://scripting/shared/functions/settimer.md)

- [ref](mta://scripting/shared/functions/ref.md)

- [deref](mta://scripting/shared/functions/deref.md)

- [sha256](mta://scripting/shared/functions/sha256.md)

- [split](mta://scripting/shared/functions/split.md)

- [teaDecode](mta://scripting/shared/functions/teadecode.md)

- [teaEncode](mta://scripting/shared/functions/teaencode.md)

- [toJSON](mta://scripting/shared/functions/tojson.md)

- [tocolor](mta://scripting/shared/functions/tocolor.md)

- [getProcessMemoryStats](mta://scripting/shared/functions/getprocessmemorystats.md)

- [utfChar](mta://scripting/shared/functions/utfchar.md)

- [utfCode](mta://scripting/shared/functions/utfcode.md)

- [utfLen](mta://scripting/shared/functions/utflen.md)

- [utfSeek](mta://scripting/shared/functions/utfseek.md)

- [utfSub](mta://scripting/shared/functions/utfsub.md)

- [bitAnd](mta://scripting/shared/functions/bitand.md)

- [bitNot](mta://scripting/shared/functions/bitnot.md)

- [bitOr](mta://scripting/shared/functions/bitor.md)

- [bitXor](mta://scripting/shared/functions/bitxor.md)

- [bitTest](mta://scripting/shared/functions/bittest.md)

- [bitLRotate](mta://scripting/shared/functions/bitlrotate.md)

- [bitRRotate](mta://scripting/shared/functions/bitrrotate.md)

- [bitLShift](mta://scripting/shared/functions/bitlshift.md)

- [bitRShift](mta://scripting/shared/functions/bitrshift.md)

- [bitArShift](mta://scripting/shared/functions/bitarshift.md)

- [bitExtract](mta://scripting/shared/functions/bitextract.md)

- [bitReplace](mta://scripting/shared/functions/bitreplace.md)
