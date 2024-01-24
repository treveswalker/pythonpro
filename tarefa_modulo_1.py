#!/usr/bin/env python
# coding: utf-8

# In[14]:


def verifica_numero(numero):
    """
    Função principal para execução da biblioteca
    """
    
    if numero % 5 == 0 and numero % 7 == 0:
        return "fizzbuzz"
    elif numero % 5 == 0:
        return "fizz"
    elif numero % 7 == 0:
        return "buzz"
    else:
        return "miss"


# In[15]:


get_ipython().system('python -m pylint tarefa_modulo_1.ipynb')


# In[16]:


get_ipython().system('python -m pycodestyle tarefa_modulo_1.ipynb')


# In[ ]:




