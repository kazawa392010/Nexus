from supabase import create_async_client

URL_SUPABASE = ""
KEY_SUPABASE = ""

supabase = create_async_client(URL_SUPABASE, KEY_SUPABASE)

async def tao_tk(name_user: str, mk_mk: str, title: str):
    try:
        list_name = await supabase.table("list_user").select("name_user").eq("name_user", name_user).execute()
        list_title = await supabase.table("list_title").select("*").eq("title", title).single().execute()
        
        if list_name.data != []:
            return f"{name_user}: Tên này tao dùng trước ròi :<"
            
        if list_title.data['so_luong'] > 0:
            await supabase.table("list_title").update({"so_luong": list_title.data['so_luong'] - 1}).eq("title", title).execute()
            data = {
                "name_user": name_user,
                "mk_user": mk_mk,
                "title": title
            }
            await supabase.table("list_user").insert(data).execute()
            return f"Successfully created account for {name_user} with title {title}"
        else:
            return "Mã khởi tạo mày nhập hết slot rùi á :>>"
    except Exception as e: 
        return f"Lỗi gì đó ròi mã khởi tạo sai chăng :? {e}"

async def dang_nhap(name_user: str, mk_user: str):
    try:
        list_user = await supabase.table("list_user").select("*").eq("name_user", name_user).single().execute()
        
        if list_user.data['mk_user'] != mk_user:
            return "Sai mk ròi kìa ní :>>"
            
        return [
            {"Welcome": f"Đăng nhập thành công! Chào mừng {name_user} :3"},
            {"name_user": name_user},
            {"title": list_user.data["title"]}
        ]
    except Exception as e:
        return f"Lỗi ròi sai mk hay name á coi lại đi hoặc có lẽ database ngủ quên:>> {e}"