import pandas as pd

class DataController:
    @staticmethod
    def load_data(file_path):
        try:
            #Lendo e tratando a planilha para uso
            df = pd.read_excel(file_path).dropna()
            df.reset_index(drop=True, inplace=True)
            df.columns = df.iloc[0]
            df = df[1:]
            df.reset_index(drop=True, inplace=True)
            return df
        
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
            return None
    
    #Recebendo dados para nova planilha e atribuindo-os
    @staticmethod
    def generate_CPU(df):
        if df is not None:
            try:
                code = df.iloc[:, 0]              # Códigos (SINAPI)
                description = df.iloc[:, 1]       # Descrição (SINAPI)
                unit = df.iloc[:, 2]              # Unidade (SINAPI)
                item_code = df.iloc[:, 3]         # Código do item (SINAPI)
                item_description = df.iloc[:, 4]  # Descrição do item (SINAPI)
                item_unit = df.iloc[:, 5]         # Unidade do item (SINAPI)
                coefficient = df.iloc[:, 6]       # Coeficiente (SINAPI)
                unit_price = df.iloc[:, 7]        # Preço unitário (SINAPI)

                newdf = pd.DataFrame({
                    "CÓDIGO DA COMPOSIÇÃO": code,
                    "DESCRIÇÃO DA COMPOSIÇÃO": description,
                    "UNIDADE": unit,
                    "CÓDIGO ITEM": item_code,
                    "DESCRIÇÃO ITEM": item_description,
                    "UNIDADE ITEM": item_unit,
                    "COEFICIENTE": coefficient,
                    "PREÇO UNITÁRIO": unit_price
                })
                return newdf
            
            except Exception as e:
                print(f"Erro ao gerar a nova planilha: {e}")
                return None
        else:
            print("O DataFrame fornecido é None.")
            return None







    @staticmethod
    def save_data(dataframe, file_path):
        try:
            dataframe.to_excel(file_path, index=False)
            print(f"Dados salvos com sucesso em {file_path}")
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")

    def process_data(df, codes):
        # Processa o DataFrame filtrando as linhas que contêm os códigos fornecidos.

        # Args:
        # - df (pd.DataFrame): O DataFrame a ser processado.
        # - codes (list): Lista de códigos para filtrar os dados.

        # Returns:
        # - pd.DataFrame: DataFrame contendo apenas as linhas correspondentes aos códigos.

        if df is None:
            print("DataFrame não carregado. Verifique o arquivo.")
            return None
        
        filtered_df = df[df['Código'].isin(codes)]
        
        # Exemplo de cálculo adicional: adicionar uma nova coluna
        if 'Quant.' in filtered_df.columns and 'Valor Unit' in filtered_df.columns:
            filtered_df['Valor Total'] = filtered_df['Quant.'] * filtered_df['Valor Unit']
        
        return filtered_df
