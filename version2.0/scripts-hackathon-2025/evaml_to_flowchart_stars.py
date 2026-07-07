from graphviz import Digraph
import os

def criar_fluxograma_robo_stars():
    # Criar o grafo direcionado
    dot = Digraph('RoboStars', comment='Fluxograma do Script do Robô Stars')
    dot.attr(rankdir='TB', size='16,20', concentrate='false')
    
    # Configurações gerais - FONTE DEJAVU SANS PARA LINUX
    dot.attr('node', fontname='DejaVu Sans', fontsize='10', height='0.6')
    dot.attr('edge', fontname='DejaVu Sans', fontsize='8', fontstyle='italic')
    
    # INÍCIO E FIM
    dot.node('start', 'Equipe: Stars (Início)', shape='ellipse', style='filled', fillcolor='white')
    dot.node('end', 'Fim', shape='ellipse', style='filled', fillcolor='white')
    
    # SEÇÃO PRINCIPAL - INÍCIO DO SCRIPT
    with dot.subgraph(name='cluster_main') as main:
        main.attr(label='', style='rounded', color='lightgray')
        
        # Elementos iniciais
        main.node('emotion1', '<<B>evaEmotion</B><BR/>emotion="HAPPY">', 
                 shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        main.node('talk1', '<<B>talk</B><BR/>"Olá, eu sou a Eva.">', 
                 shape='box', style='filled', fillcolor='lightblue', height='0.7')
        main.node('talk2', '<<B>talk</B><BR/>"Qual é o seu nome?">', 
                 shape='box', style='filled', fillcolor='lightblue', height='0.7')
        main.node('listen1', '<<B>listen</B><BR/>var="nome">', 
                 shape='box', style='filled', fillcolor='lightgreen', height='0.7')
        main.node('emotion2', '<<B>evaEmotion</B><BR/>emotion="HAPPY">', 
                 shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        main.node('talk3', '<<B>talk</B><BR/>"Olá #nome, tudo bem com você?">', 
                 shape='box', style='filled', fillcolor='lightblue', height='0.7')
        main.node('emotion3', '<<B>evaEmotion</B><BR/>emotion="NEUTRAL">', 
                 shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        
        # Sequência de luzes inicial
        main.node('light_pink', '<<B>light</B><BR/>state="ON" color="PINK">', 
                 shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        main.node('wait1', '<<B>wait</B><BR/>duration="1000">', 
                 shape='box', style='filled', fillcolor='orange', height='0.7')
        main.node('light_red', '<<B>light</B><BR/>state="ON" color="RED">', 
                 shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        main.node('wait2', '<<B>wait</B><BR/>duration="1000">', 
                 shape='box', style='filled', fillcolor='orange', height='0.7')
        main.node('light_blue', '<<B>light</B><BR/>state="ON" color="BLUE">', 
                 shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        
        # Elemento com ID - DESTACADO
        main.node('emotion_voltar', '<<B>evaEmotion</B><BR/>emotion="INLOVE"<BR/><B>id="voltar"</B>>', 
                 shape='box', style='filled', fillcolor='#FF6B6B', height='0.7') # peripheries='2'
        
        main.node('talk4', '<<B>talk</B><BR/>"Olá, você quer aprender<BR/>português ou matemática?">', 
                 shape='box', style='filled', fillcolor='lightblue', height='0.7')
        main.node('listen2', '<<B>listen</B><BR/>>', 
                 shape='box', style='filled', fillcolor='lightgreen', height='0.7')
        main.node('switch1', '<<B>switch</B><BR/>var="$">', 
                 shape='diamond', style='filled', fillcolor='plum', height='0.8')
        
        # Conexões principais
        main.edge('emotion1', 'talk1')
        main.edge('talk1', 'talk2')
        main.edge('talk2', 'listen1')
        main.edge('listen1', 'emotion2')
        main.edge('emotion2', 'talk3')
        main.edge('talk3', 'emotion3')
        main.edge('emotion3', 'light_pink')
        main.edge('light_pink', 'wait1')
        main.edge('wait1', 'light_red')
        main.edge('light_red', 'wait2')
        main.edge('wait2', 'light_blue')
        main.edge('light_blue', 'emotion_voltar')
        main.edge('emotion_voltar', 'talk4')
        main.edge('talk4', 'listen2')
        main.edge('listen2', 'switch1')
    
    # CASO PORTUGUÊS
    with dot.subgraph(name='cluster_portugues') as portugues:
        portugues.attr(label='Português', style='rounded', color='lightgray', fontsize='12')
        
        portugues.node('case_portugues', '<<B>case</B><BR/>op="contain" value="português">', 
                      shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        portugues.node('emotion_port1', '<<B>evaEmotion</B><BR/>emotion="HAPPY">', 
                      shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        portugues.node('talk_port1', '<<B>talk</B><BR/>"Eu posso te ajudar a entender<BR/>sinônimo e antônimo.">', 
                      shape='box', style='filled', fillcolor='lightblue', height='0.7')
        portugues.node('talk_port2', '<<B>talk</B><BR/>"Por qual gostaria de começar?">', 
                      shape='box', style='filled', fillcolor='lightblue', height='0.7')
        portugues.node('listen_port', '<<B>listen</B><BR/>>', 
                      shape='box', style='filled', fillcolor='lightgreen', height='0.7')
        portugues.node('switch_port', '<<B>switch</B><BR/>var="$">', 
                      shape='diamond', style='filled', fillcolor='plum', height='0.8')
        
        # Conexões português
        portugues.edge('case_portugues', 'emotion_port1')
        portugues.edge('emotion_port1', 'talk_port1')
        portugues.edge('talk_port1', 'talk_port2')
        portugues.edge('talk_port2', 'listen_port')
        portugues.edge('listen_port', 'switch_port')
    
    # SUBCASO SINÔNIMO
    with dot.subgraph(name='cluster_sinonimo') as sinonimo:
        sinonimo.attr(label='Sinônimo', style='rounded', color='lightgray', fontsize='12')
        
        sinonimo.node('case_sinonimo', '<<B>case</B><BR/>op="contain" value="sinônimo">', 
                     shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        sinonimo.node('emotion_sin', '<<B>evaEmotion</B><BR/>emotion="NEUTRAL">', 
                     shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        sinonimo.node('talk_sin1', '<<B>talk</B><BR/>"Sinônimos são as palavras que<BR/>possuem o mesmo ou<BR/>aproximadamente o mesmo<BR/>significado.">', 
                     shape='box', style='filled', fillcolor='lightblue', height='0.8')
        sinonimo.node('wait_sin', '<<B>wait</B><BR/>duration="500">', 
                     shape='box', style='filled', fillcolor='orange', height='0.7')
        sinonimo.node('talk_sin2', '<<B>talk</B><BR/>"Por exemplo, bonita é<BR/>sinônimo de linda">', 
                     shape='box', style='filled', fillcolor='lightblue', height='0.7')
        
        # Conexões sinônimo
        sinonimo.edge('case_sinonimo', 'emotion_sin')
        sinonimo.edge('emotion_sin', 'talk_sin1')
        sinonimo.edge('talk_sin1', 'wait_sin')
        sinonimo.edge('wait_sin', 'talk_sin2')
    
    # SUBCASO ANTÔNIMO
    with dot.subgraph(name='cluster_antonimo') as antonimo:
        antonimo.attr(label='Antônimo', style='rounded', color='lightgray', fontsize='12')
        
        antonimo.node('case_antonimo', '<<B>case</B><BR/>op="contain" value="antônimo">', 
                     shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        antonimo.node('talk_ant1', '<<B>talk</B><BR/>"Antônimos são palavras que<BR/>possuem significados opostos,<BR/>contrários.">', 
                     shape='box', style='filled', fillcolor='lightblue', height='0.8')
        antonimo.node('wait_ant', '<<B>wait</B><BR/>duration="500">', 
                     shape='box', style='filled', fillcolor='orange', height='0.7')
        antonimo.node('talk_ant2', '<<B>talk</B><BR/>"Por exemplo, alegre é<BR/>antônimo de triste.">', 
                     shape='box', style='filled', fillcolor='lightblue', height='0.7')
        
        # Conexões antônimo
        antonimo.edge('case_antonimo', 'talk_ant1')
        antonimo.edge('talk_ant1', 'wait_ant')
        antonimo.edge('wait_ant', 'talk_ant2')
    
    # CASO MATEMÁTICA
    with dot.subgraph(name='cluster_matematica') as matematica:
        matematica.attr(label='Matemática', style='rounded', color='lightgray', fontsize='12')
        
        matematica.node('case_matematica', '<<B>case</B><BR/>op="contain" value="matemática">', 
                       shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        matematica.node('emotion_mat1', '<<B>evaEmotion</B><BR/>emotion="HAPPY">', 
                       shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        matematica.node('talk_mat1', '<<B>talk</B><BR/>"Eu posso te ajudar com<BR/>Teorema de Pitágoras ou<BR/>Trigonometria.">', 
                       shape='box', style='filled', fillcolor='lightblue', height='0.8')
        matematica.node('wait_mat1', '<<B>wait</B><BR/>duration="500">', 
                       shape='box', style='filled', fillcolor='orange', height='0.7')
        matematica.node('talk_mat2', '<<B>talk</B><BR/>"Por qual gostaria de começar?">', 
                       shape='box', style='filled', fillcolor='lightblue', height='0.7')
        matematica.node('listen_mat', '<<B>listen</B><BR/>>', 
                       shape='box', style='filled', fillcolor='lightgreen', height='0.7')
        matematica.node('switch_mat', '<<B>switch</B><BR/>var="$">', 
                       shape='diamond', style='filled', fillcolor='plum', height='0.8')
        
        # Conexões matemática
        matematica.edge('case_matematica', 'emotion_mat1')
        matematica.edge('emotion_mat1', 'talk_mat1')
        matematica.edge('talk_mat1', 'wait_mat1')
        matematica.edge('wait_mat1', 'talk_mat2')
        matematica.edge('talk_mat2', 'listen_mat')
        matematica.edge('listen_mat', 'switch_mat')
    
    # SUBCASO PITÁGORAS
    with dot.subgraph(name='cluster_pitagoras') as pitagoras:
        pitagoras.attr(label='Pitágoras', style='rounded', color='lightgray', fontsize='12')
        
        pitagoras.node('case_pitagoras', '<<B>case</B><BR/>op="contain" value="pitágoras">', 
                      shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        pitagoras.node('talk_pit1', '<<B>talk</B><BR/>"O quadrado da medida da<BR/>hipotenusa é igual a soma<BR/>dos quadrados das medidas<BR/>dos catetos.">', 
                      shape='box', style='filled', fillcolor='lightblue', height='0.8')
        pitagoras.node('wait_pit', '<<B>wait</B><BR/>duration="500">', 
                      shape='box', style='filled', fillcolor='orange', height='0.7')
        pitagoras.node('emotion_pit', '<<B>evaEmotion</B><BR/>emotion="NEUTRAL">', 
                      shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        
        # Conexões pitágoras
        pitagoras.edge('case_pitagoras', 'talk_pit1')
        pitagoras.edge('talk_pit1', 'wait_pit')
        pitagoras.edge('wait_pit', 'emotion_pit')
    
    # SUBCASO TRIGONOMETRIA - SEQUÊNCIA COMPLETA DE LUZES
    with dot.subgraph(name='cluster_trigonometria') as trigonometria:
        trigonometria.attr(label='Trigonometria', style='rounded', color='lightgray', fontsize='12')
        
        trigonometria.node('case_trigono', '<<B>case</B><BR/>op="contain" value="trigonometria">', 
                          shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        trigonometria.node('emotion_trig1', '<<B>evaEmotion</B><BR/>emotion="HAPPY">', 
                          shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        trigonometria.node('talk_trig1', '<<B>talk</B><BR/>"Eu tenho uma música para te<BR/>ajudar na Tabela de ângulos<BR/>notáveis.">', 
                          shape='box', style='filled', fillcolor='lightblue', height='0.8')
        trigonometria.node('audio_trig', '<<B>audio</B><BR/>source="song-star-notaveis"<BR/>block="FALSE">', 
                          shape='box', style='filled', fillcolor='#6BFFB8', height='0.7')
        
        # SEQUÊNCIA COMPLETA DE LUZES (15 cores alternadas)
        # Primeira sequência
        trigonometria.node('light_green1', '<<B>light</B><BR/>state="ON" color="GREEN">', 
                          shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        trigonometria.node('wait_light1', '<<B>wait</B><BR/>duration="1000">', 
                          shape='box', style='filled', fillcolor='orange', height='0.7')
        trigonometria.node('light_red1', '<<B>light</B><BR/>state="ON" color="RED">', 
                          shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        trigonometria.node('wait_light2', '<<B>wait</B><BR/>duration="1000">', 
                          shape='box', style='filled', fillcolor='orange', height='0.7')
        trigonometria.node('light_blue1', '<<B>light</B><BR/>state="ON" color="BLUE">', 
                          shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        trigonometria.node('wait_light3', '<<B>wait</B><BR/>duration="1000">', 
                          shape='box', style='filled', fillcolor='orange', height='0.7')
        trigonometria.node('light_pink1', '<<B>light</B><BR/>state="ON" color="PINK">', 
                          shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        trigonometria.node('wait_light4', '<<B>wait</B><BR/>duration="1000">', 
                          shape='box', style='filled', fillcolor='orange', height='0.7')
        trigonometria.node('light_yellow1', '<<B>light</B><BR/>state="ON" color="YELLOW">', 
                          shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        trigonometria.node('wait_light5', '<<B>wait</B><BR/>duration="1000">', 
                          shape='box', style='filled', fillcolor='orange', height='0.7')
        
        # Segunda sequência
        trigonometria.node('light_green2', '<<B>light</B><BR/>state="ON" color="GREEN">', 
                          shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        trigonometria.node('wait_light6', '<<B>wait</B><BR/>duration="1000">', 
                          shape='box', style='filled', fillcolor='orange', height='0.7')
        trigonometria.node('light_red2', '<<B>light</B><BR/>state="ON" color="RED">', 
                          shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        trigonometria.node('wait_light7', '<<B>wait</B><BR/>duration="1000">', 
                          shape='box', style='filled', fillcolor='orange', height='0.7')
        trigonometria.node('light_blue2', '<<B>light</B><BR/>state="ON" color="BLUE">', 
                          shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        trigonometria.node('wait_light8', '<<B>wait</B><BR/>duration="1000">', 
                          shape='box', style='filled', fillcolor='orange', height='0.7')
        trigonometria.node('light_pink2', '<<B>light</B><BR/>state="ON" color="PINK">', 
                          shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        trigonometria.node('wait_light9', '<<B>wait</B><BR/>duration="1000">', 
                          shape='box', style='filled', fillcolor='orange', height='0.7')
        trigonometria.node('light_yellow2', '<<B>light</B><BR/>state="ON" color="YELLOW">', 
                          shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        trigonometria.node('wait_light10', '<<B>wait</B><BR/>duration="1000">', 
                          shape='box', style='filled', fillcolor='orange', height='0.7')
        
        # Terceira sequência
        trigonometria.node('light_green3', '<<B>light</B><BR/>state="ON" color="GREEN">', 
                          shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        trigonometria.node('wait_light11', '<<B>wait</B><BR/>duration="1000">', 
                          shape='box', style='filled', fillcolor='orange', height='0.7')
        trigonometria.node('light_red3', '<<B>light</B><BR/>state="ON" color="RED">', 
                          shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        trigonometria.node('wait_light12', '<<B>wait</B><BR/>duration="1000">', 
                          shape='box', style='filled', fillcolor='orange', height='0.7')
        trigonometria.node('light_blue3', '<<B>light</B><BR/>state="ON" color="BLUE">', 
                          shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        trigonometria.node('wait_light13', '<<B>wait</B><BR/>duration="1000">', 
                          shape='box', style='filled', fillcolor='orange', height='0.7')
        trigonometria.node('light_pink3', '<<B>light</B><BR/>state="ON" color="PINK">', 
                          shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        trigonometria.node('wait_light14', '<<B>wait</B><BR/>duration="1000">', 
                          shape='box', style='filled', fillcolor='orange', height='0.7')
        trigonometria.node('light_yellow3', '<<B>light</B><BR/>state="ON" color="YELLOW">', 
                          shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        trigonometria.node('wait_light15', '<<B>wait</B><BR/>duration="3000">', 
                          shape='box', style='filled', fillcolor='orange', height='0.7')
        
        trigonometria.node('talk_trig_final', '<<B>talk</B><BR/>"Espero que tenha gostado.<BR/>Até breve.">', 
                          shape='box', style='filled', fillcolor='lightblue', height='0.7')
        trigonometria.node('stop_trig', '<<B>stop</B>>', 
                          shape='box', style='filled', fillcolor='#E71D36', height='0.7')
        
        # Conexões trigonometria - SEQUÊNCIA COMPLETA
        trigonometria.edge('case_trigono', 'emotion_trig1')
        trigonometria.edge('emotion_trig1', 'talk_trig1')
        trigonometria.edge('talk_trig1', 'audio_trig')
        trigonometria.edge('audio_trig', 'light_green1')
        
        # Primeira sequência de luzes
        trigonometria.edge('light_green1', 'wait_light1')
        trigonometria.edge('wait_light1', 'light_red1')
        trigonometria.edge('light_red1', 'wait_light2')
        trigonometria.edge('wait_light2', 'light_blue1')
        trigonometria.edge('light_blue1', 'wait_light3')
        trigonometria.edge('wait_light3', 'light_pink1')
        trigonometria.edge('light_pink1', 'wait_light4')
        trigonometria.edge('wait_light4', 'light_yellow1')
        trigonometria.edge('light_yellow1', 'wait_light5')
        
        # Segunda sequência de luzes
        trigonometria.edge('wait_light5', 'light_green2')
        trigonometria.edge('light_green2', 'wait_light6')
        trigonometria.edge('wait_light6', 'light_red2')
        trigonometria.edge('light_red2', 'wait_light7')
        trigonometria.edge('wait_light7', 'light_blue2')
        trigonometria.edge('light_blue2', 'wait_light8')
        trigonometria.edge('wait_light8', 'light_pink2')
        trigonometria.edge('light_pink2', 'wait_light9')
        trigonometria.edge('wait_light9', 'light_yellow2')
        trigonometria.edge('light_yellow2', 'wait_light10')
        
        # Terceira sequência de luzes
        trigonometria.edge('wait_light10', 'light_green3')
        trigonometria.edge('light_green3', 'wait_light11')
        trigonometria.edge('wait_light11', 'light_red3')
        trigonometria.edge('light_red3', 'wait_light12')
        trigonometria.edge('wait_light12', 'light_blue3')
        trigonometria.edge('light_blue3', 'wait_light13')
        trigonometria.edge('wait_light13', 'light_pink3')
        trigonometria.edge('light_pink3', 'wait_light14')
        trigonometria.edge('wait_light14', 'light_yellow3')
        trigonometria.edge('light_yellow3', 'wait_light15')
        trigonometria.edge('wait_light15', 'talk_trig_final')
        trigonometria.edge('talk_trig_final', 'stop_trig')
    
    # ELEMENTOS FINAIS - ALINHADOS VERTICALMENTE (subgraph invisível)
    with dot.subgraph(name='cluster_final_invisible') as final:
        final.attr(style='invis')  # Subgraph invisível para forçar alinhamento
        
        final.node('talk_final1', '<<B>talk</B><BR/>"Espero ter ajudado.<BR/>Até breve.">', 
                  shape='box', style='filled', fillcolor='lightblue', height='0.7')
        final.node('emotion_final', '<<B>evaEmotion</B><BR/>emotion="INLOVE">', 
                  shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        final.node('goto_voltar', '<<B>goto</B><BR/>target="voltar">', 
                  shape='box', style='filled', fillcolor='white', color='black', penwidth='2', height='0.7')
        
        # Conexões seção final - FORÇANDO ALINHAMENTO VERTICAL
        final.edge('talk_final1', 'emotion_final')
        final.edge('emotion_final', 'goto_voltar')
    
    # CONEXÕES PRINCIPAIS ENTRE CLUSTERS
    
    # Conexão início
    dot.edge('start', 'emotion1')
    
    # Conexões do switch principal para os casos
    dot.edge('switch1', 'case_portugues', label='português')
    dot.edge('switch1', 'case_matematica', label='matemática')
    
    # Conexões do switch português para subcasos
    dot.edge('switch_port', 'case_sinonimo', label='sinônimo')
    dot.edge('switch_port', 'case_antonimo', label='antônimo')
    
    # Conexões do switch matemática para subcasos
    dot.edge('switch_mat', 'case_pitagoras', label='pitágoras')
    dot.edge('switch_mat', 'case_trigono', label='trigonometria')
    
    # Conexões dos subcasos de volta para os elementos finais
    dot.edge('talk_sin2', 'talk_final1')
    dot.edge('talk_ant2', 'talk_final1')
    dot.edge('emotion_pit', 'talk_final1')
    
    # ✅ CORREÇÃO: CONEXÃO DIRETA SEM NÓ INVISÍVEL (remoção do deslocamento)
    dot.edge('goto_voltar', 'emotion_voltar', style='dashed', color='blue')
    
    # Conexões finais
    dot.edge('stop_trig', 'end')
    
    return dot

def main():
    # Criar o fluxograma
    dot = criar_fluxograma_robo_stars()
    
    # Configurar o caminho de saída
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Gerar o gráfico em diferentes formatos
    print("Gerando Fluxograma - Equipe Stars...")
    
    # # Formato PNG
    # dot.render(filename=os.path.join(output_dir, 'robo_stars'), format='png', cleanup=True)
    # print("✅ PNG gerado: output/robo_stars.png")
    
    # Formato PDF
    dot.render(filename=os.path.join(output_dir, 'Fluxograma - Equipe Stars'), format='pdf', cleanup=True)
    print("✅ PDF gerado: output/Fluxograma - Equipe Stars.pdf")
    
    # # Formato SVG
    # dot.render(filename=os.path.join(output_dir, 'robo_stars'), format='svg', cleanup=True)
    # print("✅ SVG gerado: output/robo_stars.svg")
    
    # # Salvar código DOT
    # with open(os.path.join(output_dir, 'robo_stars.dot'), 'w', encoding='utf-8') as f:
    #     f.write(dot.source)
    # print("✅ Código DOT salvo: output/robo_stars.dot")
    
    # print("\n🎨 Fluxograma do Robô Stars gerado com sucesso!")
    # print("📊 Características:")
    # print("   ✅ SEQUÊNCIA COMPLETA de 15 luzes alternadas")
    # print("   ✅ 3 ciclos completos de cores: GREEN→RED→BLUE→PINK→YELLOW")
    # print("   ✅ Estrutura hierárquica com 2 níveis de menus")
    # print("   ✅ Português: Sinônimo e Antônimo")
    # print("   ✅ Matemática: Pitágoras e Trigonometria")
    # print("   ✅ Elemento com ID destacado (borda dupla)")
    # print("   ✅ Nomes dos elementos em NEGRITO")
    # print("   ✅ Fontes em DejaVu Sans com labels em itálico")
    # print("   ✅ Elementos finais ALINHADOS VERTICALMENTE")
    # print("   ✅ CONEXÃO DIRETA do goto (sem deslocamento desnecessário)")

if __name__ == "__main__":
    main()