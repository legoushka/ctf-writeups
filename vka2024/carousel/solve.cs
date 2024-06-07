using System;
using System.Collections.Generic;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        string encryptedText = "B7B04EB788419838EEDEF75AAF9B4534A764AD7EF4AD4D943B3090F4968A72";
        string decryptedHex = Decipher(encryptedText);
        Console.WriteLine("Decrypted hex: " + decryptedHex);
    }

    public static string Decipher(string inputStr)
    {
        string temp = inputStr;
        string key = "77bb234face137c4ad1e61efc0f4f6eeee6f4f0cfe16e1da4c731ecaf432bb77";
        string newkey = "bb7777bb234face137c4ad1e61efc0f4f6eeee6f4f0cfe16e1da4c731ecaf432";
        List<string> used = new List<string>();
        
        used.Insert(0, key);
        Console.WriteLine(key);
        
        List<string> usedRotateKeys = new List<string> {
            "0x77", "0x4C", "0xE1", "0xC4", "0xC0", "0xF4", "0x23", "0x37", "0xBB", "0x1E", "0x73", "0xF4", "0x23", "0x37", "0xBB", "0x1E", "0x73", "0xF4", "0x23", "0x37", "0xBB", "0x1E", "0x73", "0xF4", "0x23", "0x37", "0xBB", "0x1E", "0x73", "0xF4", "0x23"
            //, "0x37" 
        };
        
        for (int i = 0; i < usedRotateKeys.Count; i += 1)
        {
            key = RotateStr(key, Convert.ToInt32(usedRotateKeys[i], 16));
            Console.WriteLine(key);
            used.Add(key);
        }
        
        used.Reverse();
        
        for (int i = 0; i < used.Count; i += 1)
        {
            temp = XorStr(temp, used[i]);
        }
        
        
    
        
        Console.WriteLine("Used Rot Keys: " + string.Join(", ", usedRotateKeys));
        Console.WriteLine("New key:" + newkey);
        Console.WriteLine("Gen key:" + key);
        
        
        
        
    
        return temp;
    }
    
    public static List<string> Scissors(string inputStr)
    {
      List<string> result = new List<string>();
      for (int i = 0; i < inputStr.Length; i += 2)
      {
        result.Add(inputStr.Substring(i, 2));
      }
      return result;
    }
    
    public static string XorStr(string inputStr, string key)
    {
      List<string> scInput = Scissors(inputStr);
      List<string> scKey = Scissors(key);
      string newKey = "";
      for (int i = 0; i < scInput.Count; i++)
      {
        int inputVal = Convert.ToInt32(scInput[i], 16);
        int keyVal = Convert.ToInt32(scKey[i], 16);
        newKey += (inputVal ^ keyVal).ToString("X2");
      }
      return newKey;
    }
    public static string RotateStr(string inputStr, int key)
    {
      List<string> scInput = Scissors(inputStr);
      List<string> newKey = new List<string>();
      for (int i = 0; i < scInput.Count; i++)
      {
        int index = (i + key) % scInput.Count;
        newKey.Add(scInput[index]);
      }
      return string.Join("", newKey);
    }
}
