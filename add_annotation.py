import os

# 要插入的脚本标签
script_tag = "<script>(function(){window.hypothesisConfig=function(){return{showHighlights:true,appType:'bookmarklet'};};var d=document,s=d.createElement('script');s.setAttribute('src','https://hypothes.is/embed.js');d.body.appendChild(s)})();</script>"

def add_script_to_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 检查<body></body>标签中是否已经包含<script src="a.js"></script>
    if script_tag not in content:
        # 找到</body>标签的位置，并在其前插入脚本标签
        new_content = content.replace('</body>', f'{script_tag}</body>')
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)

def find_and_modify_html_files(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file == 'index.html':
                file_path = os.path.join(root, file)
                add_script_to_html(file_path)

# 指定当前目录为根目录
root_directory = '.'
find_and_modify_html_files(root_directory)
