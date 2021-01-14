import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width) 
  
    string = wrapper.fill(text=string) 
    return string
if __name__ == '__main__':