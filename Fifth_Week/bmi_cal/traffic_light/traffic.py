class Traffic:
    # def lights(red:str,yellow:str,green:str):
    #     if red:
    #         print("Please Stop")
    #     elif yellow:
    #         print("Start")
    #     elif green:
    #         print("Go!!")
    def action(color:str)->str:
        action = ""
        try:
            
            color_dict = {
                "red": "stop",
                "yellow": "ready",
                "green": "go"
            }
            # for key, value in color_dict.items():
            #     if key == color:
            #         action = [value]
            action = [value for key, value in color_dict.items() if key == color]
        except:
            print("error handle")

        else:
            print("no error")

        finally:
            return action




    

        