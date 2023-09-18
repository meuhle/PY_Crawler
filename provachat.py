import openai

api_key = "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"

openai.api_key = api_key



def get_response(messages:list):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
       messages = messages,
       # temperature = 1.0 # 0.0 - 2.0
    )
    return response.choices[0].message

if __name__ == "__main__":
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Show me at least 20 dealer that sell  robotic rehabilitation in Europe"},
        {"role": "assistant", "content": "Hocoma - Website: https://www.hocoma.com/ \n ReWalk Robotics - Website: https://rewalk.com/ \n Ekso Bionics - Website: https://eksobionics.com/ \n Bionik Laboratories - Website: http://www.bioniklabs.com/ \n Tyromotion - Website: https://www.tyromotion.com/ \n Motek Medical - Website: https://www.motekmedical.com/ \n Fourier Intelligence - Website: https://www.fourierintelligence.com/ \n Myomo - Website: https://myomo.com/ \n Reha-Stim Medtec - Website: https://www.rehastim.com/ \n Focal Meditech - Website: https://focalmeditech.nl/ \n Robosoft - Website: https://www.robosoft.com/ \n Technaid - Website: https://www.technaid.com/ \n Fysiomed - Website: https://fysiomed.org/ \n PathMaker Neurosystems - Website: https://www.pmneuro.com/ \n Cyberdyne Inc. - Website: https://www.cyberdyne.jp/ \n Hapticom - Website: https://www.hapticom.com/ \n RB3D - Website: http://www.rb3d.com/ \n Armeo by Hocoma - Website: https://www.hocoma.com/armeospring/ \n MediTouch - Website: http://www.meditouch.co.il \n MediTec International - Website: https://www.meditec.nl/"},
        {"role": "user", "content": "Give me 50 results more"}
    ]
    try:
        while True:
            user_input = input("\nTu: ")
            messages.append({"role": "user", "content": user_input})
            new_message = get_response(messages=messages)
            print(f"\nJOI: {new_message['content']}")
            messages.append(new_message)
    except KeyboardInterrupt:
        print("A presto!")
