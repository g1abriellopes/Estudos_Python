        dados_input = DadosInput().orcamento()
        produtos = ['CF_ESM', 'F_ESM', 'CAP_ESM', 'D_PROD_ESM']
        colunas_merge = ['Data Base', 'Planta', 'Quantidade']
        custo_fixo = dados_input[dados_input['Id Produto'] == 'CF_ESM']
        for produto in produtos[1:]:
            produto_data = dados_input[dados_input['Id Produto'] == produto][colunas_merge]
            coluna_suffix = f'_{produto[:3]}'
            custo_fixo = custo_fixo.merge(produto_data, on=['Data Base', 'Planta'], how='left', suffixes=('', coluna_suffix))
