# Diretrizes de Manutenção do Repositório

## 📋 Visão Geral

Este documento estabelece diretrizes para manter a qualidade e consistência da documentação do repositório da Formação Profissional em Engenharia de Dados.

## 🎯 Princípios Fundamentais

1. **Fidelidade ao Código**: A documentação deve refletir EXATAMENTE o que o código faz
2. **Didática**: Linguagem clara e acessível para alunos iniciantes e intermediários
3. **Consistência**: Todos os READMEs seguem a mesma estrutura padrão
4. **Completude**: Informações essenciais sempre presentes (instalação, execução, pré-requisitos)

## 📐 Template Padrão de README

Todos os READMEs devem seguir esta estrutura:

```markdown
# [Nome do Projeto/Módulo]

## 📋 Sobre
[Descrição clara do que é, propósito educacional, contexto]

## 🎯 Objetivos de Aprendizado
[Lista de objetivos específicos que o aluno vai alcançar]

## 📁 Estrutura do Projeto
[Árvore de diretórios com explicações breves]

## 🛠️ Tecnologias e Ferramentas
[Lista de tecnologias com propósito de cada uma]

## 📦 Pré-requisitos
[Requisitos técnicos e conhecimentos necessários]

## 🚀 Como Usar
### Instalação
[Comandos passo a passo]

### Execução
[Como executar o projeto]

## 📚 Conteúdo Real
[Descrição detalhada baseada no código real]

## 🔗 Conexões com a Formação
- Pré-requisitos: [módulos anteriores]
- Próximos passos: [módulos seguintes]

## 📖 Recursos Adicionais
[Links úteis]

## 👤 Autor
[Informações do autor]
```

## ✅ Checklist de Revisão

Antes de criar ou atualizar um README, verifique:

- [ ] Li o código do projeto antes de escrever
- [ ] A descrição reflete o que o código realmente faz
- [ ] Todos os comandos de instalação foram testados
- [ ] Os pré-requisitos estão corretos e completos
- [ ] A estrutura de pastas está atualizada
- [ ] As tecnologias listadas são realmente usadas no código
- [ ] Os links estão funcionando
- [ ] O formato segue o template padrão
- [ ] Não há promessas de funcionalidades que não existem

## 🔍 Processo de Análise

Ao adicionar ou atualizar um projeto:

1. **Leia o código primeiro**
   - Examine todos os arquivos principais
   - Entenda a estrutura e fluxo
   - Identifique tecnologias realmente usadas

2. **Execute o projeto**
   - Siga as instruções existentes
   - Documente problemas encontrados
   - Corrija instruções incorretas

3. **Escreva a documentação**
   - Use o template padrão
   - Seja específico e técnico
   - Evite linguagem genérica

4. **Valide**
   - Teste todos os comandos
   - Verifique links
   - Revise ortografia e formatação

## 🚫 Erros Comuns a Evitar

1. **Descrições genéricas**: "Este projeto faz ETL" → "Este projeto consolida arquivos Excel usando Pandas"
2. **Tecnologias não utilizadas**: Listar bibliotecas que não aparecem no código
3. **Comandos incorretos**: Copiar comandos sem testar
4. **Estrutura desatualizada**: Documentar pastas que não existem mais
5. **Promessas vazias**: "Você vai aprender X" sem explicar como

## 📝 Padrões de Escrita

### Títulos e Seções
- Use emojis consistentes (📋, 🎯, 📁, 🛠️, etc.)
- Mantenha hierarquia clara
- Seções obrigatórias sempre presentes

### Código
- Use blocos de código com syntax highlighting
- Inclua comentários explicativos quando necessário
- Teste todos os comandos antes de documentar

### Links
- Sempre use links absolutos para recursos externos
- Links internos relativos para outros módulos do repositório
- Verifique se links estão funcionando

## 🔄 Processo de Atualização

Quando o código muda:

1. **Atualize o README imediatamente**
   - Não deixe documentação desatualizada
   - Se a mudança é grande, reescreva seções inteiras

2. **Mantenha histórico**
   - Use Git para rastrear mudanças
   - Commits claros: "Atualiza README após mudança em X"

3. **Comunique mudanças**
   - Se mudanças afetam alunos, documente claramente
   - Use seção "Changelog" se necessário

## 📊 Métricas de Qualidade

Um README de qualidade deve:

- ✅ Ser compreensível por um aluno iniciante
- ✅ Permitir execução do projeto sem ajuda externa
- ✅ Refletir fielmente o código existente
- ✅ Estar formatado consistentemente
- ✅ Ter todos os links funcionando
- ✅ Incluir exemplos práticos quando relevante

## 🎓 Contexto Educacional

Lembre-se que este repositório é:

- **Material de ensino**: Deve ser didático e progressivo
- **Portfólio de projetos**: Demonstra habilidades práticas
- **Referência técnica**: Pode ser usado como consulta

Portanto:
- Explique o "porquê", não apenas o "como"
- Conecte conceitos com outros módulos
- Forneça contexto de quando usar cada técnica

## 🔗 Recursos Úteis

- Template de README: `.README_TEMPLATE.md`
- Exemplos de READMEs bem escritos: Projetos 01-05
- Guia de Markdown: [GitHub Flavored Markdown](https://github.github.com/gfm/)

## 📞 Suporte

Em caso de dúvidas sobre documentação:
- Consulte este documento primeiro
- Compare com READMEs existentes bem escritos
- Quando em dúvida, prefira clareza sobre brevidade

---

**Última atualização**: Dezembro 2024
**Mantenedor**: Equipe Jornada de Dados

