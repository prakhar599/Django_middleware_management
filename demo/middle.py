def simplemiddleware(get_response):
    
    print('one time initialisation ')
    
    def middleware(request):
        print('running before view')
        
        response= get_response(request)
        
        print('running after view')
        
        return response
    
    return middleware