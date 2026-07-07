from graphviz import Digraph
import os

def criar_fluxograma_robo_amina():
    # Criar o grafo direcionado
    dot = Digraph('Fluxograma - Equipe Âmina', comment='Fluxograma do Script do Robô Âmina')
    dot.attr(rankdir='TB', size='16,20', concentrate='false')
    
    # Configurações gerais - MESMO ESTILO
    dot.attr('node', fontname='DejaVu Sans', fontsize='10', height='0.6')
    dot.attr('edge', fontname='DejaVu Sans', fontsize='8')
    
    # INÍCIO E FIM
    dot.node('start', 'Equipe: Âmina (Início)', shape='ellipse', style='filled', fillcolor='white')
    dot.node('end', 'Fim', shape='ellipse', style='filled', fillcolor='white')
    
    # SEÇÃO PRINCIPAL - INÍCIO DO SCRIPT
    with dot.subgraph(name='cluster_main') as main:
        main.attr(label='', style='rounded', color='lightgray')
        
        # Elementos iniciais
        main.node('listen_ligar', '<<B>listen</B><BR/>var="ligar">', 
                 shape='box', style='filled', fillcolor='lightgreen', height='0.7')
        main.node('emotion1', '<<B>evaEmotion</B><BR/>emotion="HAPPY">', 
                 shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        main.node('talk1', '<<B>talk</B><BR/>"Bom dia, Maitê! O que você<BR/>gostaria de aprender hoje?">', 
                 shape='box', style='filled', fillcolor='lightblue', height='0.7')
        main.node('listen_problema', '<<B>listen</B><BR/>var="problema">', 
                 shape='box', style='filled', fillcolor='lightgreen', height='0.7')
        
        # Elemento com ID - DESTACADO
        main.node('wait_voltar', '<<B>wait</B><BR/>duration="6000"<BR/><B>id="VOLTAR"</B>>', 
                 shape='box', style='filled', fillcolor='orange', height='0.7') # peripheries='2'
        
        main.node('talk2', '<<B>talk</B><BR/>"Tudo bem! Como você deseja<BR/>aprender? Com quiz ou dicas?">', 
                 shape='box', style='filled', fillcolor='lightblue', height='0.7')
        main.node('listen_resposta', '<<B>listen</B><BR/>var="resposta">', 
                 shape='box', style='filled', fillcolor='lightgreen', height='0.7')
        main.node('switch1', '<<B>switch</B><BR/>var="resposta">', 
                 shape='diamond', style='filled', fillcolor='plum', height='0.8')
        
        # Conexões principais
        main.edge('listen_ligar', 'emotion1')
        main.edge('emotion1', 'talk1')
        main.edge('talk1', 'listen_problema')
        main.edge('listen_problema', 'wait_voltar')
        main.edge('wait_voltar', 'talk2')
        main.edge('talk2', 'listen_resposta')
        main.edge('listen_resposta', 'switch1')
    
    # MÓDULO DICAS
    with dot.subgraph(name='cluster_dicas') as dicas:
        dicas.attr(label='Dicas', style='rounded', color='lightgray', fontsize='12')
        
        dicas.node('case_dicas', '<<B>case</B><BR/>op="contain" value="dicas">', 
                  shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        dicas.node('talk_dica1', '<<B>talk</B><BR/>"Tudo bem, aqui vão algumas<BR/>dicas para te ajudar em<BR/>eletroquímica.">', 
                  shape='box', style='filled', fillcolor='lightblue', height='0.8')
        dicas.node('wait_dica', '<<B>wait</B><BR/>duration="2000">', 
                  shape='box', style='filled', fillcolor='orange', height='0.7')
        dicas.node('talk_dica2', '<<B>talk</B><BR/>"Primeiro, vá para um local<BR/>confortável, seja na praia,<BR/>na biblioteca ou em uma<BR/>praça e leve seu livro.">', 
                  shape='box', style='filled', fillcolor='lightblue', height='0.8')
        dicas.node('talk_dica3', '<<B>talk</B><BR/>"Com a ajuda do livro faça<BR/>um resumo do que você<BR/>entendeu.">', 
                  shape='box', style='filled', fillcolor='lightblue', height='0.8')
        dicas.node('goto_voltar', '<<B>goto</B><BR/>target="VOLTAR">', 
                  shape='box', style='filled', fillcolor='white', color='black', penwidth='2', height='0.7')
        
        # Conexões módulo dicas
        dicas.edge('case_dicas', 'talk_dica1')
        dicas.edge('talk_dica1', 'wait_dica')
        dicas.edge('wait_dica', 'talk_dica2')
        dicas.edge('talk_dica2', 'talk_dica3')
        dicas.edge('talk_dica3', 'goto_voltar')
    
    # MÓDULO QUIZ - PERGUNTA 1
    with dot.subgraph(name='cluster_quiz1') as quiz1:
        quiz1.attr(label='Quiz - Questão 1', style='rounded', color='lightgray', fontsize='12')
        
        quiz1.node('case_quiz', '<<B>case</B><BR/>op="contain" value="quiz">', 
                  shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        quiz1.node('talk_quiz1', '<<B>talk</B><BR/>"Tudo bem, vamos começar!">', 
                  shape='box', style='filled', fillcolor='lightblue', height='0.7')
        
        # Elemento com ID - DESTACADO
        quiz1.node('wait_tente', '<<B>wait</B><BR/>duration="1000"<BR/><B>id="TENTEDNV"</B>>', 
                  shape='box', style='filled', fillcolor='orange', height='0.7') # peripheries='2'
        
        # PERGUNTA 1
        quiz1.node('talk_pergunta1', '<<B>talk</B><BR/>"Qual é o fenômeno que ocorre<BR/>ao juntar água e sal de<BR/>cozinha separando os íons?">', 
                  shape='box', style='filled', fillcolor='lightblue', height='0.8')
        quiz1.node('talk_opcao1', '<<B>talk</B><BR/>"1, corrosão">', 
                  shape='box', style='filled', fillcolor='lightblue', height='0.7')
        quiz1.node('talk_opcao2', '<<B>talk</B><BR/>"2, redução dos íons">', 
                  shape='box', style='filled', fillcolor='lightblue', height='0.7')
        quiz1.node('talk_opcao3', '<<B>talk</B><BR/>"3, reações nucleares">', 
                  shape='box', style='filled', fillcolor='lightblue', height='0.7')
        quiz1.node('talk_opcao4', '<<B>talk</B><BR/>"4, dissociação iônica">', 
                  shape='box', style='filled', fillcolor='lightblue', height='0.7')
        
        quiz1.node('wait_quiz1', '<<B>wait</B><BR/>duration="2000">', 
                  shape='box', style='filled', fillcolor='orange', height='0.7')
        quiz1.node('listen_quiz1', '<<B>listen</B><BR/>var="respostaa">', 
                  shape='box', style='filled', fillcolor='lightgreen', height='0.7')
        quiz1.node('switch_quiz1', '<<B>switch</B><BR/>var="respostaa">', 
                  shape='diamond', style='filled', fillcolor='plum', height='0.8')
        
        # Cases do quiz 1 - INDIVIDUAIS
        quiz1.node('case_1', '<<B>case</B><BR/>op="contain" value="1">', shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        quiz1.node('case_2', '<<B>case</B><BR/>op="contain" value="2">', shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        quiz1.node('case_3', '<<B>case</B><BR/>op="contain" value="3">', shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        quiz1.node('case_4', '<<B>case</B><BR/>op="contain" value="4">', shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        quiz1.node('default_quiz1', '<default>', shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        
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
    
    # CASO 1 - RESPOSTA ERRADA (INDIVIDUAL)
    with dot.subgraph(name='cluster_errado1') as errado1:
        errado1.attr(label='Opção 1 - Errada', style='rounded', color='lightgray', fontsize='12')
        
        errado1.node('emotion_sad1', '<<B>evaEmotion</B><BR/>emotion="SAD">', 
                    shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        errado1.node('talk_erro1', '<<B>talk</B><BR/>"Você errou, deseja<BR/>encerrar ou repetir?">', 
                    shape='box', style='filled', fillcolor='lightblue', height='0.7')
        errado1.node('motion_no1', '<<B>motion</B><BR/>type="2NO">', 
                    shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        errado1.node('listen_rep1', '<<B>listen</B><BR/>var="repouenc">', 
                    shape='box', style='filled', fillcolor='lightgreen', height='0.7')
        errado1.node('switch_rep1', '<<B>switch</B><BR/>var="repouenc">', 
                    shape='diamond', style='filled', fillcolor='plum', height='0.8')
        
        # Cases repetição
        errado1.node('case_repetir1', '<<B>case</B><BR/>op="contain" value="repetir">', 
                    shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        errado1.node('case_encerrar1', '<<B>case</B><BR/>op="contain" value="encerrar">', 
                    shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        
        errado1.node('talk_repetir1', '<<B>talk</B><BR/>"vamos lá">', 
                    shape='box', style='filled', fillcolor='lightblue', height='0.7')
        errado1.node('goto_tente1', '<<B>goto</B><BR/>target="TENTEDNV">', 
                    shape='box', style='filled', fillcolor='white', color='black', penwidth='2', height='0.7')
        errado1.node('talk_proxima1', '<<B>talk</B><BR/>"vamos para a próxima<BR/>pergunta!">', 
                    shape='box', style='filled', fillcolor='lightblue', height='0.7')
        
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
    
    # CASO 2 - RESPOSTA ERRADA (INDIVIDUAL)
    with dot.subgraph(name='cluster_errado2') as errado2:
        errado2.attr(label='Opção 2 - Errada', style='rounded', color='lightgray', fontsize='12')
        
        errado2.node('emotion_sad2', '<<B>evaEmotion</B><BR/>emotion="SAD">', 
                    shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        errado2.node('talk_erro2', '<<B>talk</B><BR/>"Você errou, deseja<BR/>encerrar ou repetir?">', 
                    shape='box', style='filled', fillcolor='lightblue', height='0.7')
        errado2.node('motion_no2', '<<B>motion</B><BR/>type="2NO">', 
                    shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        errado2.node('listen_rep2', '<<B>listen</B><BR/>var="repouenc">', 
                    shape='box', style='filled', fillcolor='lightgreen', height='0.7')
        errado2.node('switch_rep2', '<<B>switch</B><BR/>var="repouenc">', 
                    shape='diamond', style='filled', fillcolor='plum', height='0.8')
        
        # Cases repetição
        errado2.node('case_repetir2', '<<B>case</B><BR/>op="contain" value="repetir">', 
                    shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        errado2.node('case_encerrar2', '<<B>case</B><BR/>op="contain" value="encerrar">', 
                    shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        
        errado2.node('talk_repetir2', '<<B>talk</B><BR/>"vamos lá">', 
                    shape='box', style='filled', fillcolor='lightblue', height='0.7')
        errado2.node('goto_tente2', '<<B>goto</B><BR/>target="TENTEDNV">', 
                    shape='box', style='filled', fillcolor='white', color='black', penwidth='2', height='0.7')
        errado2.node('talk_proxima2', '<<B>talk</B><BR/>"vamos para a próxima<BR/>pergunta!">', 
                    shape='box', style='filled', fillcolor='lightblue', height='0.7')
        
        # Conexões resposta errada
        errado2.edge('emotion_sad2', 'talk_erro2')
        errado2.edge('talk_erro2', 'motion_no2')
        errado2.edge('motion_no2', 'listen_rep2')
        errado2.edge('listen_rep2', 'switch_rep2')
        errado2.edge('switch_rep2', 'case_repetir2', label='repetir')
        errado2.edge('switch_rep2', 'case_encerrar2', label='encerrar')
        errado2.edge('case_repetir2', 'talk_repetir2')
        errado2.edge('talk_repetir2', 'goto_tente2')
        errado2.edge('case_encerrar2', 'talk_proxima2')
    
    # CASO 3 - RESPOSTA ERRADA (INDIVIDUAL)
    with dot.subgraph(name='cluster_errado3') as errado3:
        errado3.attr(label='Opção 3 - Errada', style='rounded', color='lightgray', fontsize='12')
        
        errado3.node('emotion_sad3', '<<B>evaEmotion</B><BR/>emotion="SAD">', 
                    shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        errado3.node('talk_erro3', '<<B>talk</B><BR/>"Você errou, deseja<BR/>encerrar ou repetir?">', 
                    shape='box', style='filled', fillcolor='lightblue', height='0.7')
        errado3.node('motion_no3', '<<B>motion</B><BR/>type="2NO">', 
                    shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        errado3.node('listen_rep3', '<<B>listen</B><BR/>var="repouenc">', 
                    shape='box', style='filled', fillcolor='lightgreen', height='0.7')
        errado3.node('switch_rep3', '<<B>switch</B><BR/>var="repouenc">', 
                    shape='diamond', style='filled', fillcolor='plum', height='0.8')
        
        # Cases repetição
        errado3.node('case_repetir3', '<<B>case</B><BR/>op="contain" value="repetir">', 
                    shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        errado3.node('case_encerrar3', '<<B>case</B><BR/>op="contain" value="encerrar">', 
                    shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        
        errado3.node('talk_repetir3', '<<B>talk</B><BR/>"vamos lá">', 
                    shape='box', style='filled', fillcolor='lightblue', height='0.7')
        errado3.node('goto_tente3', '<<B>goto</B><BR/>target="TENTEDNV">', 
                    shape='box', style='filled', fillcolor='white', color='black', penwidth='2', height='0.7')
        errado3.node('talk_proxima3', '<<B>talk</B><BR/>"vamos para a próxima<BR/>pergunta!">', 
                    shape='box', style='filled', fillcolor='lightblue', height='0.7')
        
        # Conexões resposta errada
        errado3.edge('emotion_sad3', 'talk_erro3')
        errado3.edge('talk_erro3', 'motion_no3')
        errado3.edge('motion_no3', 'listen_rep3')
        errado3.edge('listen_rep3', 'switch_rep3')
        errado3.edge('switch_rep3', 'case_repetir3', label='repetir')
        errado3.edge('switch_rep3', 'case_encerrar3', label='encerrar')
        errado3.edge('case_repetir3', 'talk_repetir3')
        errado3.edge('talk_repetir3', 'goto_tente3')
        errado3.edge('case_encerrar3', 'talk_proxima3')
    
    # CASE 4 (RESPOSTA CORRETA)
    with dot.subgraph(name='cluster_correto1') as correto1:
        correto1.attr(label='Opção 4 - Correta', style='rounded', color='lightgray', fontsize='12')
        
        correto1.node('emotion_happy1', '<<B>evaEmotion</B><BR/>emotion="HAPPY">', 
                     shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        correto1.node('talk_acerto1', '<<B>talk</B><BR/>"Você acertou, Parabéns!">', 
                     shape='box', style='filled', fillcolor='lightblue', height='0.7')
        correto1.node('audio1', '<<B>audio</B><BR/>source="song-beyonce"<BR/>block="FALSE">', 
                     shape='box', style='filled', fillcolor='#6BFFB8', height='0.7')
        correto1.node('motion_yes1', '<<B>motion</B><BR/>type="2YES">', 
                     shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        correto1.node('motion_shake1', '<<B>motion</B><BR/>leftArm="SHAKE2"<BR/>rightArm="SHAKE2">', 
                     shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        correto1.node('motion_yes2', '<<B>motion</B><BR/>type="2YES">', 
                     shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        correto1.node('motion_shake2', '<<B>motion</B><BR/>leftArm="SHAKE2"<BR/>rightArm="SHAKE2">', 
                     shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        
        # LIGHTS
        correto1.node('light_green1', '<<B>light</B><BR/>state="ON" color="GREEN">', 
                     shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        correto1.node('wait_light1', '<<B>wait</B><BR/>duration="1000">', 
                     shape='box', style='filled', fillcolor='orange', height='0.7')
        correto1.node('light_pink1', '<<B>light</B><BR/>state="ON" color="PINK">', 
                     shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        correto1.node('wait_light2', '<<B>wait</B><BR/>duration="1000">', 
                     shape='box', style='filled', fillcolor='orange', height='0.7')
        
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
    
    # DEFAULT QUIZ 1
    dot.node('talk_invalido1', '<<B>talk</B><BR/>"resposta inválida">', 
             shape='box', style='filled', fillcolor='lightblue', height='0.7')
    dot.node('goto_tente_default1', '<<B>goto</B><BR/>target="TENTEDNV">', 
             shape='box', style='filled', fillcolor='white', color='black', penwidth='2', height='0.7')
    dot.edge('default_quiz1', 'talk_invalido1')
    dot.edge('talk_invalido1', 'goto_tente_default1')
    
    # ... (o resto do código permanece igual para a pergunta 2)
    
    # MÓDULO QUIZ - PERGUNTA 2
    with dot.subgraph(name='cluster_quiz2') as quiz2:
        quiz2.attr(label='Quiz - Questão 2', style='rounded', color='lightgray', fontsize='12')
        
        # Elemento com ID - DESTACADO
        quiz2.node('emotion_repeat', '<<B>evaEmotion</B><BR/>emotion="NEUTRAL"<BR/><B>id="REPETE"</B>>', 
                  shape='box', style='filled', fillcolor='#FF6B6B', height='0.7') # peripheries='2'
        
        # PERGUNTA 2
        quiz2.node('talk_pergunta2', '<<B>talk</B><BR/>"Continuando, a eletroquímica<BR/>é dividida em quais<BR/>principais assuntos:">', 
                  shape='box', style='filled', fillcolor='lightblue', height='0.8')
        quiz2.node('talk_opcao2_1', '<<B>talk</B><BR/>"1, pilhas e baterias">', 
                  shape='box', style='filled', fillcolor='lightblue', height='0.7')
        quiz2.node('talk_opcao2_2', '<<B>talk</B><BR/>"2, eletrólise e baterias">', 
                  shape='box', style='filled', fillcolor='lightblue', height='0.7')
        quiz2.node('talk_opcao2_3', '<<B>talk</B><BR/>"3, baterias e correntes">', 
                  shape='box', style='filled', fillcolor='lightblue', height='0.7')
        quiz2.node('talk_opcao2_4', '<<B>talk</B><BR/>"4, pilhas e eletrólise">', 
                  shape='box', style='filled', fillcolor='lightblue', height='0.7')
        
        quiz2.node('wait_quiz2', '<<B>wait</B><BR/>duration="2000">', 
                  shape='box', style='filled', fillcolor='orange', height='0.7')
        quiz2.node('listen_quiz2', '<<B>listen</B><BR/>var="respostaaa">', 
                  shape='box', style='filled', fillcolor='lightgreen', height='0.7')
        quiz2.node('switch_quiz2', '<<B>switch</B><BR/>var="respostaaa">', 
                  shape='diamond', style='filled', fillcolor='plum', height='0.8')
        
        # Cases do quiz 2 - INDIVIDUAIS
        quiz2.node('case_quiz2_1', '<<B>case</B><BR/>op="contain" value="1">', shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        quiz2.node('case_quiz2_2', '<<B>case</B><BR/>op="contain" value="2">', shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        quiz2.node('case_quiz2_3', '<<B>case</B><BR/>op="contain" value="3">', shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        quiz2.node('case_quiz2_4', '<<B>case</B><BR/>op="contain" value="4">', shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        quiz2.node('default_quiz2', '<default>', shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        
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
    
    # CASO QUIZ 2 - RESPOSTA 1 ERRADA (INDIVIDUAL)
    with dot.subgraph(name='cluster_errado2_1') as errado2_1:
        errado2_1.attr(label='Opção 1 - Errada', style='rounded', color='lightgray', fontsize='12')
        
        errado2_1.node('emotion_sad2_1', '<<B>evaEmotion</B><BR/>emotion="SAD">', 
                      shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        errado2_1.node('talk_erro2_1', '<<B>talk</B><BR/>"Você errou, deseja<BR/>encerrar ou repetir?">', 
                      shape='box', style='filled', fillcolor='lightblue', height='0.7')
        errado2_1.node('motion_no2_1', '<<B>motion</B><BR/>type="2NO">', 
                      shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        errado2_1.node('listen_rep2_1', '<<B>listen</B><BR/>var="repouence">', 
                      shape='box', style='filled', fillcolor='lightgreen', height='0.7')
        errado2_1.node('switch_rep2_1', '<<B>switch</B><BR/>var="repouence">', 
                      shape='diamond', style='filled', fillcolor='plum', height='0.8')
        
        # Cases repetição
        errado2_1.node('case_repetir2_1', '<<B>case</B><BR/>op="contain" value="repetir">', 
                      shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        errado2_1.node('case_encerrar2_1', '<<B>case</B><BR/>op="contain" value="encerrar">', 
                      shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        
        errado2_1.node('talk_repetir2_1', '<<B>talk</B><BR/>"vamos lá">', 
                      shape='box', style='filled', fillcolor='lightblue', height='0.7')
        errado2_1.node('goto_repeat2_1', '<<B>goto</B><BR/>target="REPETE">', 
                      shape='box', style='filled', fillcolor='white', color='black', penwidth='2', height='0.7')
        errado2_1.node('talk_proxima2_1', '<<B>talk</B><BR/>"vamos para a próxima<BR/>pergunta!">', 
                      shape='box', style='filled', fillcolor='lightblue', height='0.7')
        
        # Conexões resposta errada
        errado2_1.edge('emotion_sad2_1', 'talk_erro2_1')
        errado2_1.edge('talk_erro2_1', 'motion_no2_1')
        errado2_1.edge('motion_no2_1', 'listen_rep2_1')
        errado2_1.edge('listen_rep2_1', 'switch_rep2_1')
        errado2_1.edge('switch_rep2_1', 'case_repetir2_1', label='repetir')
        errado2_1.edge('switch_rep2_1', 'case_encerrar2_1', label='encerrar')
        errado2_1.edge('case_repetir2_1', 'talk_repetir2_1')
        errado2_1.edge('talk_repetir2_1', 'goto_repeat2_1')
        errado2_1.edge('case_encerrar2_1', 'talk_proxima2_1')
    
    # CASO QUIZ 2 - RESPOSTA 2 ERRADA (INDIVIDUAL)
    with dot.subgraph(name='cluster_errado2_2') as errado2_2:
        errado2_2.attr(label='Opção 2 - Errada', style='rounded', color='lightgray', fontsize='12')
        
        errado2_2.node('emotion_sad2_2', '<<B>evaEmotion</B><BR/>emotion="SAD">', 
                      shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        errado2_2.node('talk_erro2_2', '<<B>talk</B><BR/>"Você errou, deseja<BR/>encerrar ou repetir?">', 
                      shape='box', style='filled', fillcolor='lightblue', height='0.7')
        errado2_2.node('motion_no2_2', '<<B>motion</B><BR/>type="2NO">', 
                      shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        errado2_2.node('listen_rep2_2', '<<B>listen</B><BR/>var="repouence">', 
                      shape='box', style='filled', fillcolor='lightgreen', height='0.7')
        errado2_2.node('switch_rep2_2', '<<B>switch</B><BR/>var="repouence">', 
                      shape='diamond', style='filled', fillcolor='plum', height='0.8')
        
        # Cases repetição
        errado2_2.node('case_repetir2_2', '<<B>case</B><BR/>op="contain" value="repetir">', 
                      shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        errado2_2.node('case_encerrar2_2', '<<B>case</B><BR/>op="contain" value="encerrar">', 
                      shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        
        errado2_2.node('talk_repetir2_2', '<<B>talk</B><BR/>"vamos lá">', 
                      shape='box', style='filled', fillcolor='lightblue', height='0.7')
        errado2_2.node('goto_repeat2_2', '<<B>goto</B><BR/>target="REPETE">', 
                      shape='box', style='filled', fillcolor='white', color='black', penwidth='2', height='0.7')
        errado2_2.node('talk_proxima2_2', '<<B>talk</B><BR/>"vamos para a próxima<BR/>pergunta!">', 
                      shape='box', style='filled', fillcolor='lightblue', height='0.7')
        
        # Conexões resposta errada
        errado2_2.edge('emotion_sad2_2', 'talk_erro2_2')
        errado2_2.edge('talk_erro2_2', 'motion_no2_2')
        errado2_2.edge('motion_no2_2', 'listen_rep2_2')
        errado2_2.edge('listen_rep2_2', 'switch_rep2_2')
        errado2_2.edge('switch_rep2_2', 'case_repetir2_2', label='repetir')
        errado2_2.edge('switch_rep2_2', 'case_encerrar2_2', label='encerrar')
        errado2_2.edge('case_repetir2_2', 'talk_repetir2_2')
        errado2_2.edge('talk_repetir2_2', 'goto_repeat2_2')
        errado2_2.edge('case_encerrar2_2', 'talk_proxima2_2')
    
    # CASO QUIZ 2 - RESPOSTA 3 ERRADA (INDIVIDUAL)
    with dot.subgraph(name='cluster_errado2_3') as errado2_3:
        errado2_3.attr(label='Opção 3 - Errada', style='rounded', color='lightgray', fontsize='12')
        
        errado2_3.node('emotion_sad2_3', '<<B>evaEmotion</B><BR/>emotion="SAD">', 
                      shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        errado2_3.node('talk_erro2_3', '<<B>talk</B><BR/>"Você errou, deseja<BR/>encerrar ou repetir?">', 
                      shape='box', style='filled', fillcolor='lightblue', height='0.7')
        errado2_3.node('motion_no2_3', '<<B>motion</B><BR/>type="2NO">', 
                      shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        errado2_3.node('listen_rep2_3', '<<B>listen</B><BR/>var="repouence">', 
                      shape='box', style='filled', fillcolor='lightgreen', height='0.7')
        errado2_3.node('switch_rep2_3', '<<B>switch</B><BR/>var="repouence">', 
                      shape='diamond', style='filled', fillcolor='plum', height='0.8')
        
        # Cases repetição
        errado2_3.node('case_repetir2_3', '<<B>case</B><BR/>op="contain" value="repetir">', 
                      shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        errado2_3.node('case_encerrar2_3', '<<B>case</B><BR/>op="contain" value="encerrar">', 
                      shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        
        errado2_3.node('talk_repetir2_3', '<<B>talk</B><BR/>"vamos lá">', 
                      shape='box', style='filled', fillcolor='lightblue', height='0.7')
        errado2_3.node('goto_repeat2_3', '<<B>goto</B><BR/>target="REPETE">', 
                      shape='box', style='filled', fillcolor='white', color='black', penwidth='2', height='0.7')
        errado2_3.node('talk_proxima2_3', '<<B>talk</B><BR/>"vamos para a próxima<BR/>pergunta!">', 
                      shape='box', style='filled', fillcolor='lightblue', height='0.7')
        
        # Conexões resposta errada
        errado2_3.edge('emotion_sad2_3', 'talk_erro2_3')
        errado2_3.edge('talk_erro2_3', 'motion_no2_3')
        errado2_3.edge('motion_no2_3', 'listen_rep2_3')
        errado2_3.edge('listen_rep2_3', 'switch_rep2_3')
        errado2_3.edge('switch_rep2_3', 'case_repetir2_3', label='repetir')
        errado2_3.edge('switch_rep2_3', 'case_encerrar2_3', label='encerrar')
        errado2_3.edge('case_repetir2_3', 'talk_repetir2_3')
        errado2_3.edge('talk_repetir2_3', 'goto_repeat2_3')
        errado2_3.edge('case_encerrar2_3', 'talk_proxima2_3')
    
    # CASE QUIZ 2 - RESPOSTA CORRETA (4)
    with dot.subgraph(name='cluster_correto2') as correto2:
        correto2.attr(label='Opção 4 - Correta', style='rounded', color='lightgray', fontsize='12')
        
        correto2.node('emotion_happy2', '<<B>evaEmotion</B><BR/>emotion="HAPPY">', 
                     shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        correto2.node('talk_acerto2', '<<B>talk</B><BR/>"Você acertou, Parabéns!">', 
                     shape='box', style='filled', fillcolor='lightblue', height='0.7')
        correto2.node('audio2', '<<B>audio</B><BR/>source="song-beyonce"<BR/>block="FALSE">', 
                     shape='box', style='filled', fillcolor='#6BFFB8', height='0.7')
        correto2.node('motion_yes3', '<<B>motion</B><BR/>type="2YES">', 
                     shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        correto2.node('motion_shake3', '<<B>motion</B><BR/>leftArm="SHAKE2"<BR/>rightArm="SHAKE2">', 
                     shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        correto2.node('motion_yes4', '<<B>motion</B><BR/>type="2YES">', 
                     shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        correto2.node('motion_shake4', '<<B>motion</B><BR/>leftArm="SHAKE2"<BR/>rightArm="SHAKE2">', 
                     shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        
        # LIGHTS
        correto2.node('light_green2', '<<B>light</B><BR/>state="ON" color="GREEN">', 
                     shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        correto2.node('wait_light3', '<<B>wait</B><BR/>duration="1000">', 
                     shape='box', style='filled', fillcolor='orange', height='0.7')
        correto2.node('light_pink2', '<<B>light</B><BR/>state="ON" color="PINK">', 
                     shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        correto2.node('wait_light4', '<<B>wait</B><BR/>duration="1000">', 
                     shape='box', style='filled', fillcolor='orange', height='0.7')
        
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
    
    # DEFAULT QUIZ 2
    dot.node('talk_invalido2', '<<B>talk</B><BR/>"resposta inválida">', 
             shape='box', style='filled', fillcolor='lightblue', height='0.7')
    dot.node('goto_repeat_default2', '<<B>goto</B><BR/>target="REPETE">', 
             shape='box', style='filled', fillcolor='white', color='black', penwidth='2', height='0.7')
    dot.edge('default_quiz2', 'talk_invalido2')
    dot.edge('talk_invalido2', 'goto_repeat_default2')
    
    # DEFAULT PRINCIPAL
    dot.node('default_main', '<default>', 
             shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
    dot.node('talk_invalido_main', '<<B>talk</B><BR/>"resposta inválida">', 
             shape='box', style='filled', fillcolor='lightblue', height='0.7')
    dot.node('goto_voltar_main', '<<B>goto</B><BR/>target="VOLTAR">',
             shape='box', style='filled', fillcolor='white', color='black', penwidth='2', height='0.7')
    
    # ELEMENTOS FINAIS
    dot.node('talk_final', '<<B>talk</B><BR/>"Foi um prazer estudar<BR/>com você, boa prova!">', 
             shape='box', style='filled', fillcolor='lightblue', height='0.7')
    dot.node('stop', '<<B>stop</B>>', 
             shape='box', style='filled', fillcolor='#E71D36', height='0.7')
    
    # CONEXÕES PRINCIPAIS ENTRE CLUSTERS
    
    # Conexão início
    dot.edge('start', 'listen_ligar')
    
    # Conexões do switch principal
    dot.edge('switch1', 'case_dicas', label='dicas')
    dot.edge('switch1', 'case_quiz', label='quiz')
    dot.edge('switch1', 'default_main', label='default')
    
    # Conexões default principal
    dot.edge('default_main', 'talk_invalido_main')
    dot.edge('talk_invalido_main', 'goto_voltar_main')
    dot.edge('goto_voltar_main', 'wait_voltar', style='dashed', color='blue')
    
    # Conexões dos CASES do QUIZ 1 aos seus respectivos clusters (INDIVIDUAIS)
    dot.edge('case_1', 'emotion_sad1')
    dot.edge('case_2', 'emotion_sad2')
    dot.edge('case_3', 'emotion_sad3')
    dot.edge('case_4', 'emotion_happy1')
    
    # Conexões dos CASES do QUIZ 2 aos seus respectivos clusters (INDIVIDUAIS)
    dot.edge('case_quiz2_1', 'emotion_sad2_1')
    dot.edge('case_quiz2_2', 'emotion_sad2_2')
    dot.edge('case_quiz2_3', 'emotion_sad2_3')
    dot.edge('case_quiz2_4', 'emotion_happy2')
    
    # Conexões de retorno (Goto)
    dot.edge('goto_voltar', 'wait_voltar', style='dashed', color='blue')
    dot.edge('goto_tente1', 'wait_tente', style='dashed', color='red')
    dot.edge('goto_tente2', 'wait_tente', style='dashed', color='red')
    dot.edge('goto_tente3', 'wait_tente', style='dashed', color='red')
    dot.edge('goto_tente_default1', 'wait_tente', style='dashed', color='red')
    dot.edge('goto_repeat2_1', 'emotion_repeat', style='dashed', color='purple')
    dot.edge('goto_repeat2_2', 'emotion_repeat', style='dashed', color='purple')
    dot.edge('goto_repeat2_3', 'emotion_repeat', style='dashed', color='purple')
    dot.edge('goto_repeat_default2', 'emotion_repeat', style='dashed', color='purple')
    
    # Conexões entre módulos
    dot.edge('talk_proxima1', 'emotion_repeat')
    dot.edge('talk_proxima2', 'emotion_repeat')
    dot.edge('talk_proxima3', 'emotion_repeat')
    dot.edge('wait_light2', 'emotion_repeat')
    dot.edge('talk_proxima2_1', 'talk_final')
    dot.edge('talk_proxima2_2', 'talk_final')
    dot.edge('talk_proxima2_3', 'talk_final')
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
    print("Gerando fluxograma do script Âmina...")
    
    # # Formato PNG
    # dot.render(filename=os.path.join(output_dir, 'robo_amina'), format='png', cleanup=True)
    # print("✅ PNG gerado: output/robo_amina.png")
    
    # Formato PDF
    dot.render(filename=os.path.join(output_dir, 'Fluxograma - Equipe Âmina'), format='pdf', cleanup=True)
    print("✅ PDF gerado: output/Fluxograma - Equipe Âmina.pdf")
    
    # # Formato SVG
    # dot.render(filename=os.path.join(output_dir, 'robo_amina'), format='svg', cleanup=True)
    # print("✅ SVG gerado: output/robo_amina.svg")
    
    # # Salvar código DOT
    # with open(os.path.join(output_dir, 'robo_amina.dot'), 'w', encoding='utf-8') as f:
    #     f.write(dot.source)
    # print("✅ Código DOT salvo: output/robo_amina.dot")
    
    # print("\n🎨 Fluxograma do Robô Âmina gerado com sucesso!")
    # print("📊 Características:")
    # print("   ✅ Estrutura EXATA do XML mantida")
    # print("   ✅ Casos 1, 2 e 3 mostrados INDIVIDUALMENTE")
    # print("   ✅ Nomes dos elementos em NEGRITO")
    # print("   ✅ Espaçamento aumentado entre linhas")
    # print("   ✅ Elementos com ID destacados (borda dupla)")

if __name__ == "__main__":
    main()