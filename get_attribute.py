class className:
  
  # choice_param = option1, option2, ... , optionN

  def get_something(choice_param, args):
    function_to_call = getattr('self', 'get_something_from_' + str(choice_param), default_value_if_func_does_not_exist)
    result = function_to_call(args)
    return result
    
  def get_something_from_option1(args):
    # Process using option 1
    return result
  
  def get_something_from_option2(args):
    # Process using option 1
    return result
  
  def get_something_from_optionN(args):
    # Process using option 1
    return result
  

  
