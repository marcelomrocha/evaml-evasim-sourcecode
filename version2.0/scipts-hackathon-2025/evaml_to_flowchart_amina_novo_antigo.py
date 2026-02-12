from graphviz import Digraph
import os

def criar_fluxograma_robo_amina():
    # Criar o grafo direcionado
    dot = Digraph('RoboAmina', comment='Fluxograma do Script do Robô Âmina')
    dot.attr(rankdir='TB', size='16,20', concentrate='false')
    
    # Configurações gerais - IMPORTANTE: habilitar HTML
    dot.attr('node', fontname='DejaVu Sans', fontsize='10', height='0.6')
    dot.attr('edge', fontname='DejaVu Sans', fontsize='8', fontstyle='italic')
    
    # INÍCIO E FIM
    dot.node('start', 'Equipe: Âmina (Início)', shape='ellipse', style='filled', fillcolor='white')
    dot.node('end', 'Fim', shape='ellipse', style='filled', fillcolor='white')
    
    # SEÇÃO PRINCIPAL - INÍCIO DO SCRIPT
    with dot.subgraph(name='cluster_main') as main:
        main.attr(label='', style='rounded', color='lightgray')
        
        # Elementos iniciais - COM NEGRITO
        main.node('emotion1', '<<B>evaEmotion</B><BR/>emotion="HAPPY">', 
                 shape='box', style='filled', fillcolor='#FF6B6B')
        main.node('talk1', '<<B>talk</B><BR/>"Bom dia, Maitê! O que você<BR/>gostaria de aprender hoje?">', 
                 shape='box', style='filled', fillcolor='lightblue')
        main.node('listen1', '<<B>listen</B><BR/>var="problema">', 
                 shape='box', style='filled', fillcolor='lightgreen')
        main.node('wait1', '<<B>wait</B><BR/>duration="6000"<BR/>id="VOLTAR">', 
                 shape='box', style='filled', fillcolor='orange', peripheries='2')
        main.node('talk2', '<<B>talk</B><BR/>"Tudo bem! Como você deseja<BR/>aprender? Com quiz ou dicas?">', 
                 shape='box', style='filled', fillcolor='lightblue')
        main.node('listen2', '<<B>listen</B><BR/>var="resposta">', 
                 shape='box', style='filled', fillcolor='lightgreen')
        main.node('switch1', '<<B>switch</B><BR/>var="resposta">', 
                 shape='diamond', style='filled', fillcolor='plum')
        
        # Conexões principais
        main.edge('emotion1', 'talk1')
        main.edge('talk1', 'listen1')
        main.edge('listen1', 'wait1')
        main.edge('wait1', 'talk2')
        main.edge('talk2', 'listen2')
        main.edge('listen2', 'switch1')
    
    # MÓDULO DICAS - COM NEGRITO
    with dot.subgraph(name='cluster_dicas') as dicas:
        dicas.attr(label='Dicas', style='rounded', color='blue')
        
        dicas.node('case_dicas', '<<B>case</B><BR/>op="contain" value="dicas">', 
                  shape='box', style='filled,rounded', fillcolor='plum')
        dicas.node('talk_dica1', '<<B>talk</B><BR/>"Tudo bem, aqui vão algumas<BR/>dicas para te ajudar em<BR/>eletroquímica.">', 
                  shape='box', style='filled', fillcolor='lightblue')
        dicas.node('wait_dica', '<<B>wait</B><BR/>duration="2000">', 
                  shape='box', style='filled', fillcolor='orange')
        dicas.node('talk_dica2', '<<B>talk</B><BR/>"Primeiro, vá para um local<BR/>confortável, seja na praia,<BR/>na biblioteca ou em uma<BR/>praça e leve seu livro.">', 
                  shape='box', style='filled', fillcolor='lightblue')
        dicas.node('talk_dica3', '<<B>talk</B><BR/>"Com a ajuda do livro faça<BR/>um resumo do que você<BR/>entendeu.">', 
                  shape='box', style='filled', fillcolor='lightblue')
        dicas.node('goto_voltar', '<<B>goto</B><BR/>target="VOLTAR">', 
                  shape='box', style='filled', fillcolor='white', color='black', penwidth='2')
        
        # Conexões módulo dicas
        dicas.edge('case_dicas', 'talk_dica1')
        dicas.edge('talk_dica1', 'wait_dica')
        dicas.edge('wait_dica', 'talk_dica2')
        dicas.edge('talk_dica2', 'talk_dica3')
        dicas.edge('talk_dica3', 'goto_voltar')
    
    # MÓDULO QUIZ - PERGUNTA 1 - COM NEGRITO
    with dot.subgraph(name='cluster_quiz1') as quiz1:
        quiz1.attr(label='Quiz - Pergunta 1', style='rounded', color='green')
        
        quiz1.node('case_quiz', '<<B>case</B><BR/>op="contain" value="quiz">', 
                  shape='box', style='filled,rounded', fillcolor='plum')
        quiz1.node('talk_quiz1', '<<B>talk</B><BR/>"Tudo bem, vamos começar!">', 
                  shape='box', style='filled', fillcolor='lightblue')
        quiz1.node('wait_tente', '<<B>wait</B><BR/>duration="1000"<BR/>id="TENTEDNV">', 
                  shape='box', style='filled', fillcolor='orange', peripheries='2')
        
        # PERGUNTA 1 - COM NEGRITO
        quiz1.node('talk_pergunta1', '<<B>talk</B><BR/>"Qual é o fenômeno que ocorre<BR/>ao juntar água e sal de<BR/>cozinha separando os íons?">', 
                  shape='box', style='filled', fillcolor='lightblue')
        quiz1.node('talk_opcao1', '<<B>talk</B><BR/>"1, corrosão">', 
                  shape='box', style='filled', fillcolor='lightblue')
        quiz1.node('talk_opcao2', '<<B>talk</B><BR/>"2, redução dos íons">', 
                  shape='box', style='filled', fillcolor='lightblue')
        quiz1.node('talk_opcao3', '<<B>talk</B><BR/>"3, reações nucleares">', 
                  shape='box', style='filled', fillcolor='lightblue')
        quiz1.node('talk_opcao4', '<<B>talk</B><BR/>"4, dissociação iônica">', 
                  shape='box', style='filled', fillcolor='lightblue')
        
        quiz1.node('wait_quiz1', '<<B>wait</B><BR/>duration="2000">', 
                  shape='box', style='filled', fillcolor='orange')
        quiz1.node('listen_quiz1', '<<B>listen</B><BR/>var="respostaa">', 
                  shape='box', style='filled', fillcolor='lightgreen')
        quiz1.node('switch_quiz1', '<<B>switch</B><BR/>var="respostaa">', 
                  shape='diamond', style='filled', fillcolor='plum')
        
        # Cases do quiz 1 - COM NEGRITO
        quiz1.node('case_1', '<<B>case</B><BR/>op="contain" value="1">', shape='box', style='filled,rounded', fillcolor='plum')
        quiz1.node('case_2', '<<B>case</B><BR/>op="contain" value="2">', shape='box', style='filled,rounded', fillcolor='plum')
        quiz1.node('case_3', '<<B>case</B><BR/>op="contain" value="3">', shape='box', style='filled,rounded', fillcolor='plum')
        quiz1.node('case_4', '<<B>case</B><BR/>op="contain" value="4">', shape='box', style='filled,rounded', fillcolor='plum')
        quiz1.node('default_quiz1', '<default>', shape='box', style='filled,rounded', fillcolor='plum')
        
        # Conexões quiz 1
        quiz1.edge('case_quiz', 'talk_quiz1')
        quiz1.edge('talk_quiz1', 'wait_tente')
        quiz1.edge('wait_tente', 'talk_pergunta1')
        quiz1.edge('talk_pergunta1', 'talk_opcao1')
        quiz1.edge('talk_opcao1', 'talk_opcao2')
        quiz1.edge('talk_opcao2', 'talk_opcao3')
        quiz1.edge('talk_opcao3', 'talk_opcao4')
        quiz1.edge('talk_opcao4', 'wait_quiz1')
        quiz1.edge('wait_quiz1', 'listen_quiz1')
        quiz1.edge('listen_quiz1', 'switch_quiz1')
        
        # Conexões dos cases ao switch
        quiz1.edge('switch_quiz1', 'case_1', label='1')
        quiz1.edge('switch_quiz1', 'case_2', label='2')
        quiz1.edge('switch_quiz1', 'case_3', label='3')
        quiz1.edge('switch_quiz1', 'case_4', label='4')
        quiz1.edge('switch_quiz1', 'default_quiz1', label='default')
    
    # CASES 1, 2, 3 (RESPOSTAS ERRADAS) - COM NEGRITO
    with dot.subgraph(name='cluster_errado1') as errado1:
        errado1.attr(label='Respostas 1,2,3 - Errado', style='rounded', color='red')
        
        errado1.node('emotion_sad1', '<<B>evaEmotion</B><BR/>emotion="SAD">', 
                    shape='box', style='filled', fillcolor='#FF6B6B')
        errado1.node('talk_erro1', '<<B>talk</B><BR/>"Você errou, deseja<BR/>encerrar ou repetir?">', 
                    shape='box', style='filled', fillcolor='lightblue')
        errado1.node('motion_no1', '<<B>motion</B><BR/>type="2NO">', 
                    shape='box', style='filled', fillcolor='#FFE66D')
        errado1.node('listen_rep1', '<<B>listen</B><BR/>var="repouenc">', 
                    shape='box', style='filled', fillcolor='lightgreen')
        errado1.node('switch_rep1', '<<B>switch</B><BR/>var="repouenc">', 
                    shape='diamond', style='filled', fillcolor='plum')
        
        # Cases repetição - COM NEGRITO
        errado1.node('case_repetir1', '<<B>case</B><BR/>op="contain" value="repetir">', 
                    shape='box', style='filled,rounded', fillcolor='plum')
        errado1.node('case_encerrar1', '<<B>case</B><BR/>op="contain" value="encerrar">', 
                    shape='box', style='filled,rounded', fillcolor='plum')
        
        errado1.node('talk_repetir1', '<<B>talk</B><BR/>"vamos lá">', 
                    shape='box', style='filled', fillcolor='lightblue')
        errado1.node('goto_tente1', '<<B>goto</B><BR/>target="TENTEDNV">', 
                    shape='box', style='filled', fillcolor='white', color='black', penwidth='2')
        errado1.node('talk_proxima1', '<<B>talk</B><BR/>"vamos para a próxima<BR/>pergunta!">', 
                    shape='box', style='filled', fillcolor='lightblue')
        
        # Conexões resposta errada
        errado1.edge('emotion_sad1', 'talk_erro1')
        errado1.edge('talk_erro1', 'motion_no1')
        errado1.edge('motion_no1', 'listen_rep1')
        errado1.edge('listen_rep1', 'switch_rep1')
        errado1.edge('switch_rep1', 'case_repetir1', label='repetir')
        errado1.edge('switch_rep1', 'case_encerrar1', label='encerrar')
        errado1.edge('case_repetir1', 'talk_repetir1')
        errado1.edge('talk_repetir1', 'goto_tente1')
        errado1.edge('case_encerrar1', 'talk_proxima1')
    
    # CASE 4 (RESPOSTA CORRETA) - COM NEGRITO
    with dot.subgraph(name='cluster_correto1') as correto1:
        correto1.attr(label='Resposta 4 - Correta', style='rounded', color='darkgreen')
        
        correto1.node('emotion_happy1', '<<B>evaEmotion</B><BR/>emotion="HAPPY">', 
                     shape='box', style='filled', fillcolor='#FF6B6B')
        correto1.node('talk_acerto1', '<<B>talk</B><BR/>"Você acertou, Parabéns!">', 
                     shape='box', style='filled', fillcolor='lightblue')
        correto1.node('audio1', '<<B>audio</B><BR/>source="song-beyonce"<BR/>block="FALSE">', 
                     shape='box', style='filled', fillcolor='#6BFFB8')
        correto1.node('motion_yes1', '<<B>motion</B><BR/>type="2YES">', 
                     shape='box', style='filled', fillcolor='#FFE66D')
        correto1.node('motion_shake1', '<<B>motion</B><BR/>leftArm="SHAKE2"<BR/>rightArm="SHAKE2">', 
                     shape='box', style='filled', fillcolor='#FFE66D')
        correto1.node('motion_yes2', '<<B>motion</B><BR/>type="2YES">', 
                     shape='box', style='filled', fillcolor='#FFE66D')
        correto1.node('motion_shake2', '<<B>motion</B><BR/>leftArm="SHAKE2"<BR/>rightArm="SHAKE2">', 
                     shape='box', style='filled', fillcolor='#FFE66D')
        
        # LIGHTS - COM NEGRITO
        correto1.node('light_green1', '<<B>light</B><BR/>state="ON" color="GREEN">', 
                     shape='box', style='filled', fillcolor='#FF85A1')
        correto1.node('wait_light1', '<<B>wait</B><BR/>duration="1000">', 
                     shape='box', style='filled', fillcolor='orange')
        correto1.node('light_pink1', '<<B>light</B><BR/>state="ON" color="PINK">', 
                     shape='box', style='filled', fillcolor='#FF85A1')
        correto1.node('wait_light2', '<<B>wait</B><BR/>duration="1000">', 
                     shape='box', style='filled', fillcolor='orange')
        
        # Conexões resposta correta
        correto1.edge('emotion_happy1', 'talk_acerto1')
        correto1.edge('talk_acerto1', 'audio1')
        correto1.edge('audio1', 'motion_yes1')
        correto1.edge('motion_yes1', 'motion_shake1')
        correto1.edge('motion_shake1', 'motion_yes2')
        correto1.edge('motion_yes2', 'motion_shake2')
        correto1.edge('motion_shake2', 'light_green1')
        correto1.edge('light_green1', 'wait_light1')
        correto1.edge('wait_light1', 'light_pink1')
        correto1.edge('light_pink1', 'wait_light2')
    
    # DEFAULT QUIZ 1 - COM NEGRITO
    dot.node('talk_invalido1', '<<B>talk</B><BR/>"resposta inválida">', 
             shape='box', style='filled', fillcolor='lightblue')
    dot.node('goto_tente_default1', '<<B>goto</B><BR/>target="TENTEDNV">', 
             shape='box', style='filled', fillcolor='white', color='black', penwidth='2')
    dot.edge('default_quiz1', 'talk_invalido1')
    dot.edge('talk_invalido1', 'goto_tente_default1')
    
    # MÓDULO QUIZ - PERGUNTA 2 - COM NEGRITO
    with dot.subgraph(name='cluster_quiz2') as quiz2:
        quiz2.attr(label='Quiz - Pergunta 2', style='rounded', color='purple')
        
        quiz2.node('emotion_repeat', '<<B>evaEmotion</B><BR/>emotion="NEUTRAL"<BR/>id="REPETE">', 
                  shape='box', style='filled', fillcolor='#FF6B6B', peripheries='2')
        
        # PERGUNTA 2 - COM NEGRITO
        quiz2.node('talk_pergunta2', '<<B>talk</B><BR/>"Continuando, a eletroquímica<BR/>é dividida em quais<BR/>principais assuntos:">', 
                  shape='box', style='filled', fillcolor='lightblue')
        quiz2.node('talk_opcao2_1', '<<B>talk</B><BR/>"1, pilhas e baterias">', 
                  shape='box', style='filled', fillcolor='lightblue')
        quiz2.node('talk_opcao2_2', '<<B>talk</B><BR/>"2, eletrólise e baterias">', 
                  shape='box', style='filled', fillcolor='lightblue')
        quiz2.node('talk_opcao2_3', '<<B>talk</B><BR/>"3, baterias e correntes">', 
                  shape='box', style='filled', fillcolor='lightblue')
        quiz2.node('talk_opcao2_4', '<<B>talk</B><BR/>"4, pilhas e eletrólise">', 
                  shape='box', style='filled', fillcolor='lightblue')
        
        quiz2.node('wait_quiz2', '<<B>wait</B><BR/>duration="2000">', 
                  shape='box', style='filled', fillcolor='orange')
        quiz2.node('listen_quiz2', '<<B>listen</B><BR/>var="respostaaa">', 
                  shape='box', style='filled', fillcolor='lightgreen')
        quiz2.node('switch_quiz2', '<<B>switch</B><BR/>var="respostaaa">', 
                  shape='diamond', style='filled', fillcolor='plum')
        
        # Cases do quiz 2 - COM NEGRITO
        quiz2.node('case_quiz2_1', '<<B>case</B><BR/>op="contain" value="1">', shape='box', style='filled,rounded', fillcolor='plum')
        quiz2.node('case_quiz2_2', '<<B>case</B><BR/>op="contain" value="2">', shape='box', style='filled,rounded', fillcolor='plum')
        quiz2.node('case_quiz2_3', '<<B>case</B><BR/>op="contain" value="3">', shape='box', style='filled,rounded', fillcolor='plum')
        quiz2.node('case_quiz2_4', '<<B>case</B><BR/>op="contain" value="4">', shape='box', style='filled,rounded', fillcolor='plum')
        quiz2.node('default_quiz2', '<default>', shape='box', style='filled,rounded', fillcolor='plum')
        
        # Conexões quiz 2
        quiz2.edge('emotion_repeat', 'talk_pergunta2')
        quiz2.edge('talk_pergunta2', 'talk_opcao2_1')
        quiz2.edge('talk_opcao2_1', 'talk_opcao2_2')
        quiz2.edge('talk_opcao2_2', 'talk_opcao2_3')
        quiz2.edge('talk_opcao2_3', 'talk_opcao2_4')
        quiz2.edge('talk_opcao2_4', 'wait_quiz2')
        quiz2.edge('wait_quiz2', 'listen_quiz2')
        quiz2.edge('listen_quiz2', 'switch_quiz2')
        
        # Conexões dos cases ao switch
        quiz2.edge('switch_quiz2', 'case_quiz2_1', label='1')
        quiz2.edge('switch_quiz2', 'case_quiz2_2', label='2')
        quiz2.edge('switch_quiz2', 'case_quiz2_3', label='3')
        quiz2.edge('switch_quiz2', 'case_quiz2_4', label='4')
        quiz2.edge('switch_quiz2', 'default_quiz2', label='default')
    
    # CASES QUIZ 2 - RESPOSTAS ERRADAS (1,2,3) - COM NEGRITO
    with dot.subgraph(name='cluster_errado2') as errado2:
        errado2.attr(label='Respostas 1,2,3 - Errado', style='rounded', color='red')
        
        errado2.node('emotion_sad2', '<<B>evaEmotion</B><BR/>emotion="SAD">', 
                    shape='box', style='filled', fillcolor='#FF6B6B')
        errado2.node('talk_erro2', '<<B>talk</B><BR/>"Você errou, deseja<BR/>encerrar ou repetir?">', 
                    shape='box', style='filled', fillcolor='lightblue')
        errado2.node('motion_no2', '<<B>motion</B><BR/>type="2NO">', 
                    shape='box', style='filled', fillcolor='#FFE66D')
        errado2.node('listen_rep2', '<<B>listen</B><BR/>var="repouence">', 
                    shape='box', style='filled', fillcolor='lightgreen')
        errado2.node('switch_rep2', '<<B>switch</B><BR/>var="repouence">', 
                    shape='diamond', style='filled', fillcolor='plum')
        
        # Cases repetição - COM NEGRITO
        errado2.node('case_repetir2', '<<B>case</B><BR/>op="contain" value="repetir">', 
                    shape='box', style='filled,rounded', fillcolor='plum')
        errado2.node('case_encerrar2', '<<B>case</B><BR/>op="contain" value="encerrar">', 
                    shape='box', style='filled,rounded', fillcolor='plum')
        
        errado2.node('talk_repetir2', '<<B>talk</B><BR/>"vamos lá">', 
                    shape='box', style='filled', fillcolor='lightblue')
        errado2.node('goto_repeat2', '<<B>goto</B><BR/>target="REPETE">', 
                    shape='box', style='filled', fillcolor='white', color='black', penwidth='2')
        errado2.node('talk_proxima2', '<<B>talk</B><BR/>"vamos para a próxima<BR/>pergunta!">', 
                    shape='box', style='filled', fillcolor='lightblue')
        
        # Conexões resposta errada
        errado2.edge('emotion_sad2', 'talk_erro2')
        errado2.edge('talk_erro2', 'motion_no2')
        errado2.edge('motion_no2', 'listen_rep2')
        errado2.edge('listen_rep2', 'switch_rep2')
        errado2.edge('switch_rep2', 'case_repetir2', label='repetir')
        errado2.edge('switch_rep2', 'case_encerrar2', label='encerrar')
        errado2.edge('case_repetir2', 'talk_repetir2')
        errado2.edge('talk_repetir2', 'goto_repeat2')
        errado2.edge('case_encerrar2', 'talk_proxima2')
    
    # CASE QUIZ 2 - RESPOSTA CORRETA (4) - COM NEGRITO
    with dot.subgraph(name='cluster_correto2') as correto2:
        correto2.attr(label='Resposta 4 - Correta', style='rounded', color='darkgreen')
        
        correto2.node('emotion_happy2', '<<B>evaEmotion</B><BR/>emotion="HAPPY">', 
                     shape='box', style='filled', fillcolor='#FF6B6B')
        correto2.node('talk_acerto2', '<<B>talk</B><BR/>"Você acertou, Parabéns!">', 
                     shape='box', style='filled', fillcolor='lightblue')
        correto2.node('audio2', '<<B>audio</B><BR/>source="song-beyonce"<BR/>block="FALSE">', 
                     shape='box', style='filled', fillcolor='#6BFFB8')
        correto2.node('motion_yes3', '<<B>motion</B><BR/>type="2YES">', 
                     shape='box', style='filled', fillcolor='#FFE66D')
        correto2.node('motion_shake3', '<<B>motion</B><BR/>leftArm="SHAKE2"<BR/>rightArm="SHAKE2">', 
                     shape='box', style='filled', fillcolor='#FFE66D')
        correto2.node('motion_yes4', '<<B>motion</B><BR/>type="2YES">', 
                     shape='box', style='filled', fillcolor='#FFE66D')
        correto2.node('motion_shake4', '<<B>motion</B><BR/>leftArm="SHAKE2"<BR/>rightArm="SHAKE2">', 
                     shape='box', style='filled', fillcolor='#FFE66D')
        
        # LIGHTS - COM NEGRITO
        correto2.node('light_green2', '<<B>light</B><BR/>state="ON" color="GREEN">', 
                     shape='box', style='filled', fillcolor='#FF85A1')
        correto2.node('wait_light3', '<<B>wait</B><BR/>duration="1000">', 
                     shape='box', style='filled', fillcolor='orange')
        correto2.node('light_pink2', '<<B>light</B><BR/>state="ON" color="PINK">', 
                     shape='box', style='filled', fillcolor='#FF85A1')
        correto2.node('wait_light4', '<<B>wait</B><BR/>duration="1000">', 
                     shape='box', style='filled', fillcolor='orange')
        
        # Conexões resposta correta
        correto2.edge('emotion_happy2', 'talk_acerto2')
        correto2.edge('talk_acerto2', 'audio2')
        correto2.edge('audio2', 'motion_yes3')
        correto2.edge('motion_yes3', 'motion_shake3')
        correto2.edge('motion_shake3', 'motion_yes4')
        correto2.edge('motion_yes4', 'motion_shake4')
        correto2.edge('motion_shake4', 'light_green2')
        correto2.edge('light_green2', 'wait_light3')
        correto2.edge('wait_light3', 'light_pink2')
        correto2.edge('light_pink2', 'wait_light4')
    
    # DEFAULT QUIZ 2 - COM NEGRITO
    dot.node('talk_invalido2', '<<B>talk</B><BR/>"resposta inválida">', 
             shape='box', style='filled', fillcolor='lightblue')
    dot.node('goto_repeat_default2', '<<B>goto</B><BR/>target="REPETE">', 
             shape='box', style='filled', fillcolor='white', color='black', penwidth='2')
    dot.edge('default_quiz2', 'talk_invalido2')
    dot.edge('talk_invalido2', 'goto_repeat_default2')
    
    # DEFAULT PRINCIPAL - COM NEGRITO
    dot.node('default_main', '<default>', 
             shape='box', style='filled,rounded', fillcolor='plum')
    dot.node('talk_invalido_main', '<<B>talk</B><BR/>"resposta inválida">', 
             shape='box', style='filled', fillcolor='lightblue')
    dot.node('goto_voltar_main', '<<B>goto</B><BR/>target="VOLTAR">',
             shape='box', style='filled', fillcolor='white', color='black', penwidth='2')
    
    # ELEMENTOS FINAIS - COM NEGRITO
    dot.node('talk_final', '<<B>talk</B><BR/>"Foi um prazer estudar<BR/>com você, boa prova!">', 
             shape='box', style='filled', fillcolor='lightblue')
    dot.node('stop', '<<B>stop</B>>', 
             shape='box', style='filled', fillcolor='#E71D36')
    
    # ... (o resto das conexões permanece igual)
    
    # CONEXÕES PRINCIPAIS ENTRE CLUSTERS
    
    # Conexão início
    dot.edge('start', 'emotion1')
    
    # Conexões do switch principal
    dot.edge('switch1', 'case_dicas', label='dicas')
    dot.edge('switch1', 'case_quiz', label='quiz')
    dot.edge('switch1', 'default_main', label='default')
    
    # Conexões default principal CORRIGIDAS
    dot.edge('default_main', 'talk_invalido_main')
    dot.edge('talk_invalido_main', 'goto_voltar_main')
    dot.edge('goto_voltar_main', 'wait1', style='dashed', color='blue')
    
    # Conexões dos CASES do QUIZ 1 aos seus respectivos clusters
    dot.edge('case_1', 'emotion_sad1')
    dot.edge('case_2', 'emotion_sad1')
    dot.edge('case_3', 'emotion_sad1')
    dot.edge('case_4', 'emotion_happy1')
    
    # Conexões dos CASES do QUIZ 2 aos seus respectivos clusters
    dot.edge('case_quiz2_1', 'emotion_sad2')
    dot.edge('case_quiz2_2', 'emotion_sad2')
    dot.edge('case_quiz2_3', 'emotion_sad2')
    dot.edge('case_quiz2_4', 'emotion_happy2')
    
    # Conexões de retorno (Goto)
    dot.edge('goto_voltar', 'wait1', style='dashed', color='blue')
    dot.edge('goto_tente1', 'wait_tente', style='dashed', color='red')
    dot.edge('goto_tente_default1', 'wait_tente', style='dashed', color='red')
    dot.edge('goto_repeat2', 'emotion_repeat', style='dashed', color='purple')
    dot.edge('goto_repeat_default2', 'emotion_repeat', style='dashed', color='purple')
    
    # Conexões entre módulos
    dot.edge('talk_proxima1', 'emotion_repeat')
    dot.edge('wait_light2', 'emotion_repeat')
    dot.edge('talk_proxima2', 'talk_final')
    dot.edge('wait_light4', 'talk_final')
    
    # Conexões finais
    dot.edge('talk_final', 'stop')
    dot.edge('stop', 'end')
    
    return dot

def main():
    # Criar o fluxograma
    dot = criar_fluxograma_robo_amina()
    
    # Configurar o caminho de saída
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Gerar o gráfico em diferentes formatos
    print("Gerando fluxograma...")
    
    # Formato PNG
    dot.render(filename=os.path.join(output_dir, 'robo_amina'), format='png', cleanup=True)
    print("✅ PNG gerado: output/robo_amina.png")
    
    # Formato PDF
    dot.render(filename=os.path.join(output_dir, 'robo_amina'), format='pdf', cleanup=True)
    print("✅ PDF gerado: output/robo_amina.pdf")
    
    # Formato SVG
    dot.render(filename=os.path.join(output_dir, 'robo_amina'), format='svg', cleanup=True)
    print("✅ SVG gerado: output/robo_amina.svg")
    
    # Salvar código DOT
    with open(os.path.join(output_dir, 'robo_amina.dot'), 'w', encoding='utf-8') as f:
        f.write(dot.source)
    print("✅ Código DOT salvo: output/robo_amina.dot")
    
    print("\n🎨 Fluxograma do Robô Âmina gerado com sucesso!")
    print("📊 Melhorias aplicadas:")
    print("   ✅ Nomes dos elementos em NEGRITO usando <B>")
    print("   ✅ Todos os elementos evaEmotion com retângulo")
    print("   ✅ Aspas em todos os textos dos elementos talk")
    print("   ✅ Goto adicionado no default principal")
    print("   ✅ Estrutura visual uniforme e profissional")

if __name__ == "__main__":
    main()