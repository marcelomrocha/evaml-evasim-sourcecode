from graphviz import Digraph
import os

def criar_fluxograma_divas_altivas():
    # Criar o grafo direcionado
    dot = Digraph('DivasAltivas', comment='Fluxograma do Script Divas Altivas')
    dot.attr(rankdir='TB', size='16,20', concentrate='false')
    
    # Configurações gerais - MESMO ESTILO
    dot.attr('node', fontname='DejaVu Sans', fontsize='10', height='0.6')
    dot.attr('edge', fontname='DejaVu Sans', fontsize='8', fontstyle='italic')
    
    # INÍCIO E FIM
    dot.node('start', 'Equipe: Divas Altivas (Início)', shape='ellipse', style='filled', fillcolor='white')
    dot.node('end', 'Fim', shape='ellipse', style='filled', fillcolor='white')
    
    # SEÇÃO PRINCIPAL - INÍCIO DO SCRIPT
    with dot.subgraph(name='cluster_main') as main:
        main.attr(label='', style='rounded', color='lightgray')
        
        # Elementos iniciais
        main.node('talk1', '<<B>talk</B><BR/>"Oi, eu sou a Eva!">', 
                 shape='box', style='filled', fillcolor='lightblue', height='0.7')
        main.node('emotion1', '<<B>evaEmotion</B><BR/>emotion="HAPPY">', 
                 shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        main.node('led1', '<<B>led</B><BR/>animation="RAINBOW">', 
                 shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        main.node('wait1', '<<B>wait</B><BR/>duration="4000">', 
                 shape='box', style='filled', fillcolor='orange', height='0.7')
        main.node('talk2', '<<B>talk</B><BR/>"Me fale o seu nome.">', 
                 shape='box', style='filled', fillcolor='lightblue', height='0.7')
        main.node('listen1', '<<B>listen</B><BR/>var="nome">', 
                 shape='box', style='filled', fillcolor='lightgreen', height='0.7')
        main.node('emotion2', '<<B>evaEmotion</B><BR/>emotion="INLOVE">', 
                 shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        main.node('talk3', '<<B>talk</B><BR/>"Prazer #nome">', 
                 shape='box', style='filled', fillcolor='lightblue', height='0.7')
        main.node('talk4', '<<B>talk</B><BR/>"fiquei sabendo que você tem um<BR/>grande problema em relação a timidez.">', 
                 shape='box', style='filled', fillcolor='lightblue', height='0.7')
        main.node('talk5', '<<B>talk</B><BR/>"Preparei um jogo para você!">', 
                 shape='box', style='filled', fillcolor='lightblue', height='0.7')
        
        # Elemento com ID - DESTACADO
        main.node('talk_volta', '<<B>talk</B><BR/>"escolha um cartão"<BR/><B>id="volta"</B>>', 
                 shape='box', style='filled', fillcolor='lightblue', height='0.7') # peripheries='2'
        
        main.node('emotion3', '<<B>evaEmotion</B><BR/>emotion="NEUTRAL">', 
                 shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        main.node('qrread', '<<B>qrRead</B><BR/>var="cartao">', 
                 shape='box', style='filled', fillcolor='#E6E6FA', height='0.7')
        main.node('switch1', '<<B>switch</B><BR/>var="cartao">', 
                 shape='diamond', style='filled', fillcolor='plum', height='0.8')
        
        # Conexões principais
        main.edge('talk1', 'emotion1')
        main.edge('emotion1', 'led1')
        main.edge('led1', 'wait1')
        main.edge('wait1', 'talk2')
        main.edge('talk2', 'listen1')
        main.edge('listen1', 'emotion2')
        main.edge('emotion2', 'talk3')
        main.edge('talk3', 'talk4')
        main.edge('talk4', 'talk5')
        main.edge('talk5', 'talk_volta')
        main.edge('talk_volta', 'emotion3')
        main.edge('emotion3', 'qrread')
        main.edge('qrread', 'switch1')
    
    # CASO DANÇAR (value="dançar")
    with dot.subgraph(name='cluster_dancar') as dancar:
        dancar.attr(label='Cartão: dançar', style='rounded', color='lightgray', fontsize='12')
        
        dancar.node('case_dancar', '<<B>case</B><BR/>op="exact" value="dançar">', 
                   shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        dancar.node('talk_dancar', '<<B>talk</B><BR/>"vamos dançar comigo!">', 
                   shape='box', style='filled', fillcolor='lightblue', height='0.7')
        dancar.node('emotion_dancar', '<<B>evaEmotion</B><BR/>emotion="HAPPY">', 
                   shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        dancar.node('audio_dancar', '<<B>audio</B><BR/>source="song-macarena-edit"<BR/>block="FALSE">', 
                   shape='box', style='filled', fillcolor='#6BFFB8', height='0.7')
        dancar.node('led_dancar1', '<<B>led</B><BR/>animation="RAINBOW">', 
                   shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        
        # Sequência de movimentos - GRUPO 1
        dancar.node('motion_head1', '<<B>motion</B><BR/>head="2YES">', 
                   shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        dancar.node('motion_left1', '<<B>motion</B><BR/>leftArm="SHAKE1">', 
                   shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        dancar.node('motion_right1', '<<B>motion</B><BR/>rightArm="SHAKE2">', 
                   shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        dancar.node('wait_dancar1', '<<B>wait</B><BR/>duration="5000">', 
                   shape='box', style='filled', fillcolor='orange', height='0.7')
        
        # Sequência de movimentos - GRUPO 2
        dancar.node('motion_head2', '<<B>motion</B><BR/>head="2YES">', 
                   shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        dancar.node('motion_left2', '<<B>motion</B><BR/>leftArm="SHAKE1">', 
                   shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        dancar.node('motion_right2', '<<B>motion</B><BR/>rightArm="SHAKE2">', 
                   shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        dancar.node('wait_dancar2', '<<B>wait</B><BR/>duration="5000">', 
                   shape='box', style='filled', fillcolor='orange', height='0.7')
        
        # Sequência de movimentos - GRUPO 3
        dancar.node('led_dancar2', '<<B>led</B><BR/>animation="RAINBOW">', 
                   shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        dancar.node('motion_head3', '<<B>motion</B><BR/>head="2YES">', 
                   shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        dancar.node('motion_left3', '<<B>motion</B><BR/>leftArm="SHAKE1">', 
                   shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        dancar.node('motion_right3', '<<B>motion</B><BR/>rightArm="SHAKE2">', 
                   shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        dancar.node('wait_dancar3', '<<B>wait</B><BR/>duration="5000">', 
                   shape='box', style='filled', fillcolor='orange', height='0.7')
        
        # Sequência de movimentos - GRUPO 4
        dancar.node('motion_head4', '<<B>motion</B><BR/>head="2YES">', 
                   shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        dancar.node('motion_left4', '<<B>motion</B><BR/>leftArm="SHAKE1">', 
                   shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        dancar.node('motion_right4', '<<B>motion</B><BR/>rightArm="SHAKE2">', 
                   shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        dancar.node('wait_dancar4', '<<B>wait</B><BR/>duration="5000">', 
                   shape='box', style='filled', fillcolor='orange', height='0.7')
        
        # Sequência de movimentos - GRUPO 5
        dancar.node('motion_head5', '<<B>motion</B><BR/>head="2YES">', 
                   shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        dancar.node('motion_left5', '<<B>motion</B><BR/>leftArm="SHAKE1">', 
                   shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        dancar.node('motion_right5', '<<B>motion</B><BR/>rightArm="SHAKE2">', 
                   shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        dancar.node('wait_dancar5', '<<B>wait</B><BR/>duration="8000">', 
                   shape='box', style='filled', fillcolor='orange', height='0.7')
        
        dancar.node('led_dancar3', '<<B>led</B><BR/>animation="RAINBOW">', 
                   shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        
        # Conexões caso dançar
        dancar.edge('case_dancar', 'talk_dancar')
        dancar.edge('talk_dancar', 'emotion_dancar')
        dancar.edge('emotion_dancar', 'audio_dancar')
        dancar.edge('audio_dancar', 'led_dancar1')
        
        # Grupo 1
        dancar.edge('led_dancar1', 'motion_head1')
        dancar.edge('motion_head1', 'motion_left1')
        dancar.edge('motion_left1', 'motion_right1')
        dancar.edge('motion_right1', 'wait_dancar1')
        
        # Grupo 2
        dancar.edge('wait_dancar1', 'motion_head2')
        dancar.edge('motion_head2', 'motion_left2')
        dancar.edge('motion_left2', 'motion_right2')
        dancar.edge('motion_right2', 'wait_dancar2')
        
        # Grupo 3
        dancar.edge('wait_dancar2', 'led_dancar2')
        dancar.edge('led_dancar2', 'motion_head3')
        dancar.edge('motion_head3', 'motion_left3')
        dancar.edge('motion_left3', 'motion_right3')
        dancar.edge('motion_right3', 'wait_dancar3')
        
        # Grupo 4
        dancar.edge('wait_dancar3', 'motion_head4')
        dancar.edge('motion_head4', 'motion_left4')
        dancar.edge('motion_left4', 'motion_right4')
        dancar.edge('motion_right4', 'wait_dancar4')
        
        # Grupo 5
        dancar.edge('wait_dancar4', 'motion_head5')
        dancar.edge('motion_head5', 'motion_left5')
        dancar.edge('motion_left5', 'motion_right5')
        dancar.edge('motion_right5', 'wait_dancar5')
        dancar.edge('wait_dancar5', 'led_dancar3')
    
    # CASO CANTAR
    with dot.subgraph(name='cluster_cantar') as cantar:
        cantar.attr(label='Cartão: cantar', style='rounded', color='lightgray', fontsize='12')
        
        cantar.node('case_cantar', '<<B>case</B><BR/>op="exact" value="cantar">', 
                   shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        cantar.node('talk_cantar1', '<<B>talk</B><BR/>"Vamos cantar juntos?">', 
                   shape='box', style='filled', fillcolor='lightblue', height='0.7')
        cantar.node('light_cantar', '<<B>light</B><BR/>state="ON" color="PINK">', 
                   shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        cantar.node('audio_cantar', '<<B>audio</B><BR/>source="song-happy"<BR/>block="FALSE">', 
                   shape='box', style='filled', fillcolor='#6BFFB8', height='0.7')
        cantar.node('emotion_cantar1', '<<B>evaEmotion</B><BR/>emotion="SURPRISE">', 
                   shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        cantar.node('wait_cantar', '<<B>wait</B><BR/>duration="6000">', 
                   shape='box', style='filled', fillcolor='orange', height='0.7')
        cantar.node('light_off', '<<B>light</B><BR/>state="OFF">', 
                   shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        cantar.node('emotion_cantar2', '<<B>evaEmotion</B><BR/>emotion="HAPPY">', 
                   shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        
        # Conexões caso cantar
        cantar.edge('case_cantar', 'talk_cantar1')
        cantar.edge('talk_cantar1', 'light_cantar')
        cantar.edge('light_cantar', 'audio_cantar')
        cantar.edge('audio_cantar', 'emotion_cantar1')
        cantar.edge('emotion_cantar1', 'wait_cantar')
        cantar.edge('wait_cantar', 'light_off')
        cantar.edge('light_off', 'emotion_cantar2')
    
    # CASO PIADA
    with dot.subgraph(name='cluster_piada') as piada:
        piada.attr(label='Cartão: piada', style='rounded', color='lightgray', fontsize='12')
        
        piada.node('case_piada', '<<B>case</B><BR/>op="exact" value="piada">', 
                  shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        piada.node('talk_piada1', '<<B>talk</B><BR/>"vou contar uma piada">', 
                  shape='box', style='filled', fillcolor='lightblue', height='0.7')
        piada.node('talk_piada2', '<<B>talk</B><BR/>"Por que a velhinha não<BR/>usa relógio?">', 
                  shape='box', style='filled', fillcolor='lightblue', height='0.7')
        piada.node('audio_piada1', '<<B>audio</B><BR/>source="efx-tic-toc"<BR/>block="TRUE">', 
                  shape='box', style='filled', fillcolor='#6BFFB8', height='0.7')
        piada.node('talk_piada3', '<<B>talk</B><BR/>"Porque ela é sem hora.">', 
                  shape='box', style='filled', fillcolor='lightblue', height='0.7')
        piada.node('emotion_piada', '<<B>evaEmotion</B><BR/>emotion="HAPPY">', 
                  shape='box', style='filled', fillcolor='#FF6B6B', height='0.7')
        piada.node('motion_piada', '<<B>motion</B><BR/>head="2YES">', 
                  shape='box', style='filled', fillcolor='#FFE66D', height='0.7')
        piada.node('audio_piada2', '<<B>audio</B><BR/>source="efx-trombone-triste"<BR/>block="TRUE">', 
                  shape='box', style='filled', fillcolor='#6BFFB8', height='0.7')
        
        # Conexões caso piada
        piada.edge('case_piada', 'talk_piada1')
        piada.edge('talk_piada1', 'talk_piada2')
        piada.edge('talk_piada2', 'audio_piada1')
        piada.edge('audio_piada1', 'talk_piada3')
        piada.edge('talk_piada3', 'emotion_piada')
        piada.edge('emotion_piada', 'motion_piada')
        piada.edge('motion_piada', 'audio_piada2')
    
    # SEÇÃO FINAL - APÓS O SWITCH
    with dot.subgraph(name='cluster_final') as final:
        final.attr(label='', style='rounded', color='lightgray')
        
        final.node('talk_final1', '<<B>talk</B><BR/>"vocẽ deseja escolher<BR/>mais um cartão?">', 
                  shape='box', style='filled', fillcolor='lightblue', height='0.7')
        final.node('listen_final', '<<B>listen</B><BR/>var="Resposta">', 
                  shape='box', style='filled', fillcolor='lightgreen', height='0.7')
        final.node('switch_final', '<<B>switch</B><BR/>var="Resposta">', 
                  shape='diamond', style='filled', fillcolor='plum', height='0.8')
        
        # Cases do switch final
        final.node('case_sim', '<<B>case</B><BR/>op="contain" value="Sim">', 
                  shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        final.node('goto_volta', '<<B>goto</B><BR/>target="volta">', 
                  shape='box', style='filled', fillcolor='white', color='black', penwidth='2', height='0.7')
        
        final.node('default_final', '<default>', 
                  shape='box', style='filled,rounded', fillcolor='plum', height='0.7')
        final.node('talk_default', '<<B>talk</B><BR/>"tudo bem!">', 
                  shape='box', style='filled', fillcolor='lightblue', height='0.7')
        
        # Elementos finais
        final.node('talk_final2', '<<B>talk</B><BR/>"Espero que eu tenha te<BR/>ajudado, #nome!">', 
                  shape='box', style='filled', fillcolor='lightblue', height='0.7')
        final.node('talk_final3', '<<B>talk</B><BR/>"até a próxima!">', 
                  shape='box', style='filled', fillcolor='lightblue', height='0.7')
        final.node('audio_final', '<<B>audio</B><BR/>source="efx-aplausos-bom"<BR/>block="FALSE">', 
                  shape='box', style='filled', fillcolor='#6BFFB8', height='0.7')
        final.node('led_final', '<<B>led</B><BR/>animation="RAINBOW">', 
                  shape='box', style='filled', fillcolor='#FF85A1', height='0.7')
        
        # Conexões seção final
        final.edge('talk_final1', 'listen_final')
        final.edge('listen_final', 'switch_final')
        final.edge('switch_final', 'case_sim', label='Sim')
        final.edge('switch_final', 'default_final', label='default')
        final.edge('case_sim', 'goto_volta')
        final.edge('default_final', 'talk_default')
        final.edge('talk_default', 'talk_final2')
        final.edge('talk_final2', 'talk_final3')
        final.edge('talk_final3', 'audio_final')
        final.edge('audio_final', 'led_final')
    
    # CONEXÕES PRINCIPAIS ENTRE CLUSTERS
    
    # Conexão início
    dot.edge('start', 'talk1')
    
    # Conexões do switch principal para os casos
    dot.edge('switch1', 'case_dancar', label='dançar')
    dot.edge('switch1', 'case_cantar', label='cantar')
    dot.edge('switch1', 'case_piada', label='piada')
    
    # Conexões dos casos de volta para a seção final
    dot.edge('led_dancar3', 'talk_final1')
    dot.edge('emotion_cantar2', 'talk_final1')
    dot.edge('audio_piada2', 'talk_final1')
    
    # Conexão de retorno (Goto)
    dot.edge('goto_volta', 'talk_volta', style='dashed', color='blue')
    
    # Conexões finais
    dot.edge('led_final', 'end')
    
    return dot

def main():
    # Criar o fluxograma
    dot = criar_fluxograma_divas_altivas()
    
    # Configurar o caminho de saída
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Gerar o gráfico em diferentes formatos
    print("Gerando fluxograma do Divas Altivas...")
    
    # # Formato PNG
    # dot.render(filename=os.path.join(output_dir, 'divas_altivas'), format='png', cleanup=True)
    # print("✅ PNG gerado: output/divas_altivas.png")
    
    # # Formato PDF
    dot.render(filename=os.path.join(output_dir, 'Fluxograma - Equipe Divas Altivas'), format='pdf', cleanup=True)
    print("✅ PDF gerado: output/Fluxograma - Equipe Divas Altivas.pdf")
    
    # # Formato SVG
    # dot.render(filename=os.path.join(output_dir, 'divas_altivas'), format='svg', cleanup=True)
    # print("✅ SVG gerado: output/divas_altivas.svg")
    
    # # Salvar código DOT
    # with open(os.path.join(output_dir, 'divas_altivas.dot'), 'w', encoding='utf-8') as f:
    #     f.write(dot.source)
    # print("✅ Código DOT salvo: output/divas_altivas.dot")
    
    # print("\n🎨 Fluxograma do Robô Divas Altivas gerado com sucesso!")
    # print("📊 Características:")
    # print("   ✅ Mesmo estilo visual consistente")
    # print("   ✅ 3 opções de cartões: dançar, cantar, piada")
    # print("   ✅ Removido caso redundante 'dancar' (sem acento)")
    # print("   ✅ Nomes dos elementos em NEGRITO")
    # print("   ✅ Espaçamento aumentado entre linhas")
    # print("   ✅ Elemento com ID destacado (borda dupla)")

if __name__ == "__main__":
    main()